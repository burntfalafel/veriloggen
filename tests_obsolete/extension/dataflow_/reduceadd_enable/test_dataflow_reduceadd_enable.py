from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_reduceadd_enable

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg xvalid;
  wire xready;
  reg [1-1:0] resetdata;
  reg resetvalid;
  wire resetready;
  reg [1-1:0] enabledata;
  reg enablevalid;
  wire enableready;
  wire [32-1:0] zdata;
  wire zvalid;
  reg zready;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .resetdata(resetdata),
    .resetvalid(resetvalid),
    .resetready(resetready),
    .enabledata(enabledata),
    .enablevalid(enablevalid),
    .enableready(enableready),
    .zdata(zdata),
    .zvalid(zvalid),
    .zready(zready)
  );

  reg reset_done;

  initial begin
    $dumpfile("dataflow_reduceadd_enable.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
    xdata = 0;
    xvalid = 0;
    enabledata = 0;
    enablevalid = 0;
    resetdata = 0;
    resetvalid = 0;
    zready = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;
  localparam xfsm_7 = 7;
  localparam xfsm_8 = 8;
  localparam xfsm_9 = 9;
  localparam xfsm_10 = 10;
  localparam xfsm_11 = 11;
  localparam xfsm_12 = 12;
  localparam xfsm_13 = 13;
  localparam xfsm_14 = 14;
  localparam xfsm_15 = 15;
  localparam xfsm_16 = 16;
  localparam xfsm_17 = 17;
  localparam xfsm_18 = 18;
  localparam xfsm_19 = 19;
  localparam xfsm_20 = 20;
  localparam xfsm_21 = 21;
  localparam xfsm_22 = 22;
  localparam xfsm_23 = 23;
  localparam xfsm_24 = 24;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          xvalid <= 0;
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          xfsm <= xfsm_2;
        end
        xfsm_2: begin
          xfsm <= xfsm_3;
        end
        xfsm_3: begin
          xfsm <= xfsm_4;
        end
        xfsm_4: begin
          xfsm <= xfsm_5;
        end
        xfsm_5: begin
          xfsm <= xfsm_6;
        end
        xfsm_6: begin
          xfsm <= xfsm_7;
        end
        xfsm_7: begin
          xfsm <= xfsm_8;
        end
        xfsm_8: begin
          xfsm <= xfsm_9;
        end
        xfsm_9: begin
          xfsm <= xfsm_10;
        end
        xfsm_10: begin
          xfsm <= xfsm_11;
        end
        xfsm_11: begin
          xvalid <= 1;
          xfsm <= xfsm_12;
        end
        xfsm_12: begin
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 5) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 5) && xready) begin
            xfsm <= xfsm_13;
          end 
        end
        xfsm_13: begin
          xfsm <= xfsm_14;
        end
        xfsm_14: begin
          xfsm <= xfsm_15;
        end
        xfsm_15: begin
          xfsm <= xfsm_16;
        end
        xfsm_16: begin
          xfsm <= xfsm_17;
        end
        xfsm_17: begin
          xfsm <= xfsm_18;
        end
        xfsm_18: begin
          xfsm <= xfsm_19;
        end
        xfsm_19: begin
          xfsm <= xfsm_20;
        end
        xfsm_20: begin
          xfsm <= xfsm_21;
        end
        xfsm_21: begin
          xfsm <= xfsm_22;
        end
        xfsm_22: begin
          xfsm <= xfsm_23;
        end
        xfsm_23: begin
          xvalid <= 1;
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 20) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 20) && xready) begin
            xfsm <= xfsm_24;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  localparam zfsm_1 = 1;
  localparam zfsm_2 = 2;
  localparam zfsm_3 = 3;
  localparam zfsm_4 = 4;
  localparam zfsm_5 = 5;
  localparam zfsm_6 = 6;
  localparam zfsm_7 = 7;
  localparam zfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
    end else begin
      case(zfsm)
        zfsm_init: begin
          zready <= 0;
          if(reset_done) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          if(zvalid) begin
            zready <= 1;
          end 
          if(zvalid) begin
            zfsm <= zfsm_3;
          end 
        end
        zfsm_3: begin
          zready <= 0;
          zfsm <= zfsm_4;
        end
        zfsm_4: begin
          zready <= 0;
          zfsm <= zfsm_5;
        end
        zfsm_5: begin
          zready <= 0;
          zfsm <= zfsm_6;
        end
        zfsm_6: begin
          zready <= 0;
          zfsm <= zfsm_7;
        end
        zfsm_7: begin
          zready <= 0;
          zfsm <= zfsm_8;
        end
        zfsm_8: begin
          zfsm <= zfsm_2;
        end
      endcase
    end
  end

  reg [32-1:0] enable;
  localparam enable_init = 0;
  reg [32-1:0] enable_count;
  localparam enable_1 = 1;
  localparam enable_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      enable <= enable_init;
      enable_count <= 0;
    end else begin
      case(enable)
        enable_init: begin
          if(reset_done) begin
            enable <= enable_1;
          end 
        end
        enable_1: begin
          enablevalid <= 1;
          if(enablevalid && enableready) begin
            enable_count <= enable_count + 1;
          end 
          if(enablevalid && enableready && (enable_count == 2)) begin
            enabledata <= 1;
          end 
          if(enablevalid && enableready && (enable_count == 2)) begin
            enable <= enable_2;
          end 
        end
        enable_2: begin
          if(enablevalid && enableready) begin
            enabledata <= 0;
          end 
          enable_count <= 0;
          if(enablevalid && enableready) begin
            enable <= enable_1;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] reset;
  localparam reset_init = 0;
  reg [32-1:0] reset_count;
  localparam reset_1 = 1;
  localparam reset_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      reset <= reset_init;
      reset_count <= 0;
    end else begin
      case(reset)
        reset_init: begin
          if(reset_done) begin
            reset <= reset_1;
          end 
        end
        reset_1: begin
          resetvalid <= 1;
          if(resetvalid && resetready) begin
            reset_count <= reset_count + 1;
          end 
          if(resetvalid && resetready && (reset_count == 2)) begin
            resetdata <= 0;
          end 
          if(resetvalid && resetready && (reset_count == 2)) begin
            reset <= reset_2;
          end 
        end
        reset_2: begin
          if(resetvalid && resetready) begin
            resetdata <= 0;
          end 
          reset_count <= 0;
          if(resetvalid && resetready) begin
            reset <= reset_1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(xvalid && xready) begin
        $display("xdata=%d", xdata);
      end 
      if(zvalid && zready) begin
        $display("zdata=%d", zdata);
      end 
    end 
  end


endmodule



module main
(
  input CLK,
  input RST,
  input [32-1:0] xdata,
  input xvalid,
  output xready,
  input [1-1:0] resetdata,
  input resetvalid,
  output resetready,
  input [1-1:0] enabledata,
  input enablevalid,
  output enableready,
  output [32-1:0] zdata,
  output zvalid,
  input zready
);

  reg [32-1:0] _dataflow_reduceadd_data_4;
  reg _dataflow_reduceadd_valid_4;
  wire _dataflow_reduceadd_ready_4;
  assign enableready = (_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xvalid && enablevalid && resetvalid);
  assign xready = (_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xvalid && enablevalid && resetvalid);
  assign resetready = (_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xvalid && enablevalid && resetvalid);
  assign zdata = _dataflow_reduceadd_data_4;
  assign zvalid = _dataflow_reduceadd_valid_4;
  assign _dataflow_reduceadd_ready_4 = zready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_reduceadd_data_4 <= 1'sd0;
      _dataflow_reduceadd_valid_4 <= 0;
    end else begin
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xready && enableready && resetready) && (xvalid && enablevalid && resetvalid) && enabledata) begin
        _dataflow_reduceadd_data_4 <= _dataflow_reduceadd_data_4 + xdata;
      end 
      if(_dataflow_reduceadd_valid_4 && _dataflow_reduceadd_ready_4) begin
        _dataflow_reduceadd_valid_4 <= 0;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xready && enableready && resetready)) begin
        _dataflow_reduceadd_valid_4 <= xvalid && enablevalid && resetvalid;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xready && enableready && resetready) && (xvalid && enablevalid && resetvalid) && resetdata) begin
        _dataflow_reduceadd_data_4 <= 1'sd0;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (xready && enableready && resetready) && (xvalid && enablevalid && resetvalid) && enabledata && resetdata) begin
        _dataflow_reduceadd_data_4 <= 1'sd0 + xdata;
      end 
    end
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_reduceadd_enable.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
