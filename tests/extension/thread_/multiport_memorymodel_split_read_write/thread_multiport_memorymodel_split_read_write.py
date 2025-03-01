from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10

    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    # If RAM is simultaneously accesseed with DMA, numports must be 2 or more.
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth, numports=2)

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth)

    all_ok = m.TmpReg(initval=0)

    def blink(size):
        # wait start
        saxi.wait_flag(0, value=1, resetvalue=0)
        # reset done
        saxi.write(1, 0)

        all_ok.value = True

        for i in range(4):
            print('# iter %d start' % i)
            # Test for 4KB boundary check
            offset = i * 1024 * 16 + (myaxi.boundary_size - 4)
            body(size, offset)
            print('# iter %d end' % i)

        if all_ok:
            print('# verify (local): PASSED')
        else:
            print('# verify (local): FAILED')

        # result
        saxi.write(2, all_ok)

        # done
        saxi.write_flag(1, 1, resetvalue=0)

    def body(size, offset):
        # write
        for i in range(size):
            wdata = i + 100
            myram.write(i, wdata)

        w_laddr = 0
        w_gaddr = offset
        # If RAM is simultaneously accesseed with DMA, different port must be
        # used.
        myaxi.dma_write_async(myram, w_laddr, w_gaddr, size, port=1)
        print('dma_write_async: [%d] -> [%d]' % (w_laddr, w_gaddr))

        # write
        for i in range(size):
            wdata = i + 1000
            myram.write(i + size, wdata)

        myaxi.dma_wait_write()
        print('dma_wait_write : [%d] -> [%d]' % (w_laddr, w_gaddr))

        w_laddr = size
        w_gaddr = (size + size) * 4 + offset
        myaxi.dma_write_async(myram, w_laddr, w_gaddr, size, port=1)
        print('dma_write_async: [%d] -> [%d]' % (w_laddr, w_gaddr))

        # read
        r_laddr = 0
        r_gaddr = offset
        myaxi.dma_read_async(myram, r_laddr, r_gaddr, size, port=0)
        print('dma_read_async : [%d] <- [%d]' % (r_laddr, r_gaddr))

        for sleep in range(size):
            pass

        myaxi.dma_wait_write()
        print('dma_wait_write : [%d] -> [%d]' % (w_laddr, w_gaddr))

        myaxi.dma_wait_read()
        print('dma_wait_read  : [%d] <- [%d]' % (r_laddr, r_gaddr))

        for i in range(size):
            rdata = myram.read(i)
            if vthread.verilog.NotEql(rdata, i + 100):
                print('rdata[%d] = %d' % (i, rdata))
                all_ok.value = False

        # read
        r_laddr = 0
        r_gaddr = (size + size) * 4 + offset
        myaxi.dma_read(myram, r_laddr, r_gaddr, size, port=0)
        print('dma_read       : [%d] <- [%d]' % (r_laddr, r_gaddr))

        for sleep in range(size):
            pass

        for i in range(size):
            rdata = myram.read(i)
            if vthread.verilog.NotEql(rdata, i + 1000):
                print('rdata[%d] = %d' % (i, rdata))
                all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(32)

    return m


def mkTest(memimg_name=None):
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMultiportMemoryModel(m, 'memory', clk, rst, numports=2,
                                         memimg_name=memimg_name)

    r_ports, w_ports = axi.split_read_write(m, ports, 'myaxi')

    memory.connect(0, r_ports, 'r_myaxi')
    memory.connect(1, w_ports, 'w_myaxi')

    # AXI-Slave controller
    _saxi = vthread.AXIMLite(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(ports, 'saxi')

    def ctrl():
        for i in range(100):
            pass

        for i in range(16):
            # byte addressing
            v = memory.read(i * 4)
            print('read:  mem[%d] -> %x' % (i, v))
            v = v + 1024
            # byte addressing
            memory.write(i * 4, v)
            print('write: mem[%d] <- %x' % (i, v))

        awaddr = 0
        _saxi.write(awaddr, 1)

        araddr = 4
        v = _saxi.read(araddr)
        while v == 0:
            v = _saxi.read(araddr)

        araddr = 8
        v = _saxi.read(araddr)
        if v:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    # simulation.setup_waveform(m, uut, dumpfile=vcd_name)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000),
        Systask('finish'),
    )

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    if outputfile is None:
        outputfile = os.path.splitext(os.path.basename(__file__))[0] + '.out'

    memimg_name = 'memimg_' + outputfile

    test = mkTest(memimg_name=memimg_name)

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=outputfile)
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
