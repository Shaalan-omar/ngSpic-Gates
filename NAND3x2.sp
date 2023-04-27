.include /Users/omarshaalan/Documents/sky130_fd_pr_ngspice/sky130.sp

.subckt NAND3x2 a b c y vdd gnd
 X1 y a vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
 X2 y b vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
 X3 y c vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
 X4 y a f f sky130_fd_pr__nfet_01v8 W=3000000u L=150000u
 X5 f b g g sky130_fd_pr__nfet_01v8 W=3000000u L=150000u
 X6 g c gnd gnd sky130_fd_pr__nfet_01v8 W=3000000u L=150000u
.ends



vdd vdd gnd 1.8v
vina a gnd PULSE 0 1.8 0ps 0.1ns 0.1ns 5ns 10ns
vinb b gnd PULSE 0 1.8 0ps 0.1ns 0.1ns 5ns 10ns
vinc c gnd PULSE 0 1.8 0ps 0.1ns 0.1ns 5ns 10ns

X1 a b c y vdd gnd NAND3x2
CL1 y gnd 1fF

.tran 10ps 15ns

.control
 run
 set color0=white
 set color1=black
 set xbrushwidth=2
 plot v(a),v(b),v(y)
 meas tran tpdr
 + TRIG v(a) VAL=0.9 FALL=1
 + TARG v(y) VAL=0.9 RISE=1
 meas tran tpdf
 + TRIG v(a) VAL=0.9 RISE=1
 + TARG v(y) VAL=0.9 FALL=1
.endc