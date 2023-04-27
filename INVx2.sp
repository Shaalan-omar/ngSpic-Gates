
.include /Users/omarshaalan/Documents/sky130_fd_pr_ngspice/sky130.sp

.subckt INVx2 a b vdd gnd 
 X1 b a vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
 X2 b a gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
.ends

vdd vdd gnd 1.8v
vin x gnd PULSE 0 1.8 0ps 0.1ns 0.1ns 2.5ns 5ns
X1 x y vdd gnd INVx2
CL1 y gnd 1fF

.tran 10ps 10ns

.control
  run 
 set color0=white
 set color1=black
 set xbrushwidth=2
 plot v(x), v(y)
 meas tran tpdr 
 + TRIG v(x) VAL=0.9 FALL=1
 + TARG v(y) VAL=0.9 RISE=1
 meas tran tpdf 
 + TRIG v(x) VAL=0.9 RISE=1
 + TARG v(y) VAL=0.9 FALL=1
.endc