from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_unbalanced_outputs

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg xvalid;
  wire xready;
  reg [32-1:0] ydata;
  reg yvalid;
  wire yready;
  wire [32-1:0] z2data;
  wire z2valid;
  reg z2ready;
  wire [32-1:0] z1data;
  wire z1valid;
  reg z1ready;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .ydata(ydata),
    .yvalid(yvalid),
    .yready(yready),
    .z2data(z2data),
    .z2valid(z2valid),
    .z2ready(z2ready),
    .z1data(z1data),
    .z1valid(z1valid),
    .z1ready(z1ready)
  );

  reg reset_done;

  initial begin
    $dumpfile("dataflow_unbalanced_outputs.vcd");
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
    ydata = 0;
    yvalid = 0;
    z1ready = 0;
    z2ready = 0;
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
          if((_tmp_0 == 10) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 10) && xready) begin
            xfsm <= xfsm_24;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] _tmp_1;
  localparam yfsm_1 = 1;
  localparam yfsm_2 = 2;
  localparam yfsm_3 = 3;
  localparam yfsm_4 = 4;
  localparam yfsm_5 = 5;
  localparam yfsm_6 = 6;
  localparam yfsm_7 = 7;
  localparam yfsm_8 = 8;
  localparam yfsm_9 = 9;
  localparam yfsm_10 = 10;
  localparam yfsm_11 = 11;
  localparam yfsm_12 = 12;
  localparam yfsm_13 = 13;
  localparam yfsm_14 = 14;
  localparam yfsm_15 = 15;
  localparam yfsm_16 = 16;
  localparam yfsm_17 = 17;
  localparam yfsm_18 = 18;
  localparam yfsm_19 = 19;
  localparam yfsm_20 = 20;
  localparam yfsm_21 = 21;
  localparam yfsm_22 = 22;
  localparam yfsm_23 = 23;
  localparam yfsm_24 = 24;
  localparam yfsm_25 = 25;
  localparam yfsm_26 = 26;
  localparam yfsm_27 = 27;
  localparam yfsm_28 = 28;
  localparam yfsm_29 = 29;
  localparam yfsm_30 = 30;
  localparam yfsm_31 = 31;
  localparam yfsm_32 = 32;
  localparam yfsm_33 = 33;
  localparam yfsm_34 = 34;
  localparam yfsm_35 = 35;
  localparam yfsm_36 = 36;
  localparam yfsm_37 = 37;
  localparam yfsm_38 = 38;
  localparam yfsm_39 = 39;
  localparam yfsm_40 = 40;
  localparam yfsm_41 = 41;
  localparam yfsm_42 = 42;
  localparam yfsm_43 = 43;
  localparam yfsm_44 = 44;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
      _tmp_1 <= 0;
    end else begin
      case(yfsm)
        yfsm_init: begin
          yvalid <= 0;
          if(reset_done) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          yfsm <= yfsm_2;
        end
        yfsm_2: begin
          yfsm <= yfsm_3;
        end
        yfsm_3: begin
          yfsm <= yfsm_4;
        end
        yfsm_4: begin
          yfsm <= yfsm_5;
        end
        yfsm_5: begin
          yfsm <= yfsm_6;
        end
        yfsm_6: begin
          yfsm <= yfsm_7;
        end
        yfsm_7: begin
          yfsm <= yfsm_8;
        end
        yfsm_8: begin
          yfsm <= yfsm_9;
        end
        yfsm_9: begin
          yfsm <= yfsm_10;
        end
        yfsm_10: begin
          yfsm <= yfsm_11;
        end
        yfsm_11: begin
          yfsm <= yfsm_12;
        end
        yfsm_12: begin
          yfsm <= yfsm_13;
        end
        yfsm_13: begin
          yfsm <= yfsm_14;
        end
        yfsm_14: begin
          yfsm <= yfsm_15;
        end
        yfsm_15: begin
          yfsm <= yfsm_16;
        end
        yfsm_16: begin
          yfsm <= yfsm_17;
        end
        yfsm_17: begin
          yfsm <= yfsm_18;
        end
        yfsm_18: begin
          yfsm <= yfsm_19;
        end
        yfsm_19: begin
          yfsm <= yfsm_20;
        end
        yfsm_20: begin
          yfsm <= yfsm_21;
        end
        yfsm_21: begin
          yvalid <= 1;
          yfsm <= yfsm_22;
        end
        yfsm_22: begin
          if(yready) begin
            ydata <= ydata + 2;
          end 
          if(yready) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((_tmp_1 == 5) && yready) begin
            yvalid <= 0;
          end 
          if((_tmp_1 == 5) && yready) begin
            yfsm <= yfsm_23;
          end 
        end
        yfsm_23: begin
          yfsm <= yfsm_24;
        end
        yfsm_24: begin
          yfsm <= yfsm_25;
        end
        yfsm_25: begin
          yfsm <= yfsm_26;
        end
        yfsm_26: begin
          yfsm <= yfsm_27;
        end
        yfsm_27: begin
          yfsm <= yfsm_28;
        end
        yfsm_28: begin
          yfsm <= yfsm_29;
        end
        yfsm_29: begin
          yfsm <= yfsm_30;
        end
        yfsm_30: begin
          yfsm <= yfsm_31;
        end
        yfsm_31: begin
          yfsm <= yfsm_32;
        end
        yfsm_32: begin
          yfsm <= yfsm_33;
        end
        yfsm_33: begin
          yfsm <= yfsm_34;
        end
        yfsm_34: begin
          yfsm <= yfsm_35;
        end
        yfsm_35: begin
          yfsm <= yfsm_36;
        end
        yfsm_36: begin
          yfsm <= yfsm_37;
        end
        yfsm_37: begin
          yfsm <= yfsm_38;
        end
        yfsm_38: begin
          yfsm <= yfsm_39;
        end
        yfsm_39: begin
          yfsm <= yfsm_40;
        end
        yfsm_40: begin
          yfsm <= yfsm_41;
        end
        yfsm_41: begin
          yfsm <= yfsm_42;
        end
        yfsm_42: begin
          yfsm <= yfsm_43;
        end
        yfsm_43: begin
          yvalid <= 1;
          if(yready) begin
            ydata <= ydata + 2;
          end 
          if(yready) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((_tmp_1 == 10) && yready) begin
            yvalid <= 0;
          end 
          if((_tmp_1 == 10) && yready) begin
            yfsm <= yfsm_44;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] z1fsm;
  localparam z1fsm_init = 0;
  localparam z1fsm_1 = 1;
  localparam z1fsm_2 = 2;
  localparam z1fsm_3 = 3;
  localparam z1fsm_4 = 4;
  localparam z1fsm_5 = 5;
  localparam z1fsm_6 = 6;
  localparam z1fsm_7 = 7;
  localparam z1fsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      z1fsm <= z1fsm_init;
    end else begin
      case(z1fsm)
        z1fsm_init: begin
          z1ready <= 0;
          if(reset_done) begin
            z1fsm <= z1fsm_1;
          end 
        end
        z1fsm_1: begin
          z1fsm <= z1fsm_2;
        end
        z1fsm_2: begin
          if(z1valid) begin
            z1ready <= 1;
          end 
          if(z1valid) begin
            z1fsm <= z1fsm_3;
          end 
        end
        z1fsm_3: begin
          z1ready <= 0;
          z1fsm <= z1fsm_4;
        end
        z1fsm_4: begin
          z1ready <= 0;
          z1fsm <= z1fsm_5;
        end
        z1fsm_5: begin
          z1ready <= 0;
          z1fsm <= z1fsm_6;
        end
        z1fsm_6: begin
          z1ready <= 0;
          z1fsm <= z1fsm_7;
        end
        z1fsm_7: begin
          z1ready <= 0;
          z1fsm <= z1fsm_8;
        end
        z1fsm_8: begin
          z1fsm <= z1fsm_2;
        end
      endcase
    end
  end

  reg [32-1:0] z2fsm;
  localparam z2fsm_init = 0;
  localparam z2fsm_1 = 1;
  localparam z2fsm_2 = 2;
  localparam z2fsm_3 = 3;
  localparam z2fsm_4 = 4;
  localparam z2fsm_5 = 5;
  localparam z2fsm_6 = 6;
  localparam z2fsm_7 = 7;
  localparam z2fsm_8 = 8;
  localparam z2fsm_9 = 9;
  localparam z2fsm_10 = 10;
  localparam z2fsm_11 = 11;
  localparam z2fsm_12 = 12;
  localparam z2fsm_13 = 13;

  always @(posedge CLK) begin
    if(RST) begin
      z2fsm <= z2fsm_init;
    end else begin
      case(z2fsm)
        z2fsm_init: begin
          z2ready <= 0;
          if(reset_done) begin
            z2fsm <= z2fsm_1;
          end 
        end
        z2fsm_1: begin
          z2fsm <= z2fsm_2;
        end
        z2fsm_2: begin
          if(z2valid) begin
            z2ready <= 1;
          end 
          if(z2valid) begin
            z2fsm <= z2fsm_3;
          end 
        end
        z2fsm_3: begin
          z2ready <= 0;
          z2fsm <= z2fsm_4;
        end
        z2fsm_4: begin
          z2ready <= 0;
          z2fsm <= z2fsm_5;
        end
        z2fsm_5: begin
          z2ready <= 0;
          z2fsm <= z2fsm_6;
        end
        z2fsm_6: begin
          z2ready <= 0;
          z2fsm <= z2fsm_7;
        end
        z2fsm_7: begin
          z2ready <= 0;
          z2fsm <= z2fsm_8;
        end
        z2fsm_8: begin
          z2ready <= 0;
          z2fsm <= z2fsm_9;
        end
        z2fsm_9: begin
          z2ready <= 0;
          z2fsm <= z2fsm_10;
        end
        z2fsm_10: begin
          z2ready <= 0;
          z2fsm <= z2fsm_11;
        end
        z2fsm_11: begin
          z2ready <= 0;
          z2fsm <= z2fsm_12;
        end
        z2fsm_12: begin
          z2ready <= 0;
          z2fsm <= z2fsm_13;
        end
        z2fsm_13: begin
          z2fsm <= z2fsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(xvalid && xready) begin
        $display("xdata=%d", xdata);
      end 
      if(yvalid && yready) begin
        $display("ydata=%d", ydata);
      end 
      if(z1valid && z1ready) begin
        $display("z1data=%d", z1data);
      end 
      if(z2valid && z2ready) begin
        $display("z2data=%d", z2data);
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
  input [32-1:0] ydata,
  input yvalid,
  output yready,
  output [32-1:0] z2data,
  output z2valid,
  input z2ready,
  output [32-1:0] z1data,
  output z1valid,
  input z1ready
);

  reg [32-1:0] _dataflow_plus_data_2;
  reg _dataflow_plus_valid_2;
  wire _dataflow_plus_ready_2;
  assign xready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid);
  reg [32-1:0] _dataflow__delay_data_4;
  reg _dataflow__delay_valid_4;
  wire _dataflow__delay_ready_4;
  assign yready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid) && ((_dataflow__delay_ready_4 || !_dataflow__delay_valid_4) && yvalid);
  reg [32-1:0] _dataflow_minus_data_3;
  reg _dataflow_minus_valid_3;
  wire _dataflow_minus_ready_3;
  assign _dataflow__delay_ready_4 = (_dataflow_minus_ready_3 || !_dataflow_minus_valid_3) && (_dataflow_plus_valid_2 && _dataflow__delay_valid_4);
  reg [32-1:0] _dataflow__delay_data_5;
  reg _dataflow__delay_valid_5;
  wire _dataflow__delay_ready_5;
  assign _dataflow_plus_ready_2 = (_dataflow_minus_ready_3 || !_dataflow_minus_valid_3) && (_dataflow_plus_valid_2 && _dataflow__delay_valid_4) && ((_dataflow__delay_ready_5 || !_dataflow__delay_valid_5) && _dataflow_plus_valid_2);
  assign z2data = _dataflow_minus_data_3;
  assign z2valid = _dataflow_minus_valid_3;
  assign _dataflow_minus_ready_3 = z2ready;
  assign z1data = _dataflow__delay_data_5;
  assign z1valid = _dataflow__delay_valid_5;
  assign _dataflow__delay_ready_5 = z1ready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_plus_data_2 <= 0;
      _dataflow_plus_valid_2 <= 0;
      _dataflow__delay_data_4 <= 0;
      _dataflow__delay_valid_4 <= 0;
      _dataflow_minus_data_3 <= 0;
      _dataflow_minus_valid_3 <= 0;
      _dataflow__delay_data_5 <= 0;
      _dataflow__delay_valid_5 <= 0;
    end else begin
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready) && (xvalid && yvalid)) begin
        _dataflow_plus_data_2 <= xdata + ydata;
      end 
      if(_dataflow_plus_valid_2 && _dataflow_plus_ready_2) begin
        _dataflow_plus_valid_2 <= 0;
      end 
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready)) begin
        _dataflow_plus_valid_2 <= xvalid && yvalid;
      end 
      if((_dataflow__delay_ready_4 || !_dataflow__delay_valid_4) && yready && yvalid) begin
        _dataflow__delay_data_4 <= ydata;
      end 
      if(_dataflow__delay_valid_4 && _dataflow__delay_ready_4) begin
        _dataflow__delay_valid_4 <= 0;
      end 
      if((_dataflow__delay_ready_4 || !_dataflow__delay_valid_4) && yready) begin
        _dataflow__delay_valid_4 <= yvalid;
      end 
      if((_dataflow_minus_ready_3 || !_dataflow_minus_valid_3) && (_dataflow_plus_ready_2 && _dataflow__delay_ready_4) && (_dataflow_plus_valid_2 && _dataflow__delay_valid_4)) begin
        _dataflow_minus_data_3 <= _dataflow_plus_data_2 - _dataflow__delay_data_4;
      end 
      if(_dataflow_minus_valid_3 && _dataflow_minus_ready_3) begin
        _dataflow_minus_valid_3 <= 0;
      end 
      if((_dataflow_minus_ready_3 || !_dataflow_minus_valid_3) && (_dataflow_plus_ready_2 && _dataflow__delay_ready_4)) begin
        _dataflow_minus_valid_3 <= _dataflow_plus_valid_2 && _dataflow__delay_valid_4;
      end 
      if((_dataflow__delay_ready_5 || !_dataflow__delay_valid_5) && _dataflow_plus_ready_2 && _dataflow_plus_valid_2) begin
        _dataflow__delay_data_5 <= _dataflow_plus_data_2;
      end 
      if(_dataflow__delay_valid_5 && _dataflow__delay_ready_5) begin
        _dataflow__delay_valid_5 <= 0;
      end 
      if((_dataflow__delay_ready_5 || !_dataflow__delay_valid_5) && _dataflow_plus_ready_2) begin
        _dataflow__delay_valid_5 <= _dataflow_plus_valid_2;
      end 
    end
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_unbalanced_outputs.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
