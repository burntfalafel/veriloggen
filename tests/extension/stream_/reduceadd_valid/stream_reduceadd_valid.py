from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.stream as stream


def mkMain():
    # input variiable
    x = stream.Variable('xdata')
    y = stream.Variable('ydata')

    # stream definition
    z = x + y
    z, v = stream.ReduceAddValid(z, 8)

    # set output attribute
    z.output('zdata')
    v.output('vdata')

    st = stream.Stream(z, v,
                       ivalid='ivalid', ovalid='ovalid')
    m = st.to_module('main')

    return m


def mkTest(numports=8):
    m = Module('test')

    # target instance
    main = mkMain()

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    xdata = ports['xdata']
    ydata = ports['ydata']
    zdata = ports['zdata']
    vdata = ports['vdata']

    ivalid = ports['ivalid']
    ovalid = ports['ovalid']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))
    reset_stmt.append(xdata(0))
    reset_stmt.append(ydata(0))
    reset_stmt.append(ivalid(0))

    # vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    # simulation.setup_waveform(m, uut, dumpfile=vcd_name)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(10000),
        Systask('finish'),
    )

    send_fsm = FSM(m, 'send_fsm', clk, rst)
    send_count = m.Reg('send_count', 32, initval=0)
    send_fsm.If(reset_done).goto_next()

    send_fsm(
        ivalid(0),
        send_count.inc()
    )

    send_fsm.If(send_count == 10)(
        send_count(0)
    )
    send_fsm.If(send_count == 10).goto_next()

    send_fsm(
        xdata(0),
        ydata(0),
        ivalid(1),
        send_count.inc()
    )
    send_fsm.Delay(1)(
        Display('xdata=%d', xdata),
        Display('ydata=%d', ydata)
    )
    send_fsm.goto_next()

    send_fsm(
        xdata(xdata + 1),
        ydata(ydata + 2),
        ivalid(1),
        send_count.inc()
    )
    send_fsm.Delay(1)(
        Display('xdata=%d', xdata),
        Display('ydata=%d', ydata)
    )
    send_fsm.If(send_count == 65)(
        ivalid(0)
    )
    send_fsm.If(send_count == 65).goto_next()

    recv_fsm = FSM(m, 'recv_fsm', clk, rst)
    recv_count = m.Reg('recv_count', 32, initval=0)
    recv_fsm.If(reset_done).goto_next()

    recv_fsm.If(ovalid, vdata)(
        Display('zdata=%d', zdata),
        recv_count.inc()
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run()  # display=False
    #rslt = sim.run(display=True)
    print(rslt)

    # launch waveform viewer (GTKwave)
    # sim.view_waveform() # background=False
    # sim.view_waveform(background=True)
