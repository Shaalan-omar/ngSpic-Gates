.include /Users/omarshaalan/Documents/sky130_fd_pr_ngspice/sky130.sp
.subckt NANDx2 a b y vdd gnd
 X1 y a vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u *size of 2
 X2 y b vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u *size of 2 
 X3 y a n1 gnd sky130_fd_pr__nfet_01v8 W=1680000u L=150000u *size of 2
 X4 n1 b gnd gnd sky130_fd_pr__nfet_01v8 W=1680000u L=150000u *size of 2
.ends


vdd vdd gnd 1.8v
vina a gnd PULSE 0 1.8 0ps 0.1ns 0.1ns 2.5ns 5ns
vinb b gnd PULSE 0 1.8 0ps 0.1ns 0.1ns 5ns 10ns


X1 a b y vdd gnd NANDx2
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