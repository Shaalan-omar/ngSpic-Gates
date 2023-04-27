.include /Users/omarshaalan/Documents/sky130_fd_pr_ngspice/sky130.sp


.subckt Nor3x2 in1 in2 in3 out vdd gnd
X1 w1 in1 vdd vdd sky130_fd_pr__pfet_01v8 W=7000000u L=150000u 
X2 w2 in2 w1 w1 sky130_fd_pr__pfet_01v8 W=7000000u L=150000u 
X3 out in3 w2 w2 sky130_fd_pr__pfet_01v8 W=7000000u L=150000u 

X4 out in1 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
X5 out in2 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
X6 out in3 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
.ends

vdd vdd gnd 1.8v
vinin1 in1 gnd PULSE 0 1.8 0ps 0ps 0ps 5ns 10ns
vinin2 in2 gnd PULSE 0 1.8 0ps 0ps 0ps 5ns 10ns
vinin3 in3 gnd PULSE 0 1.8 0ps 0ps 0ps 5ns 10ns
X1 in1 in2 in3 out vdd gnd Nor3x2
CL1 out gnd 1fF

.tran 10ps 20ns
.control
 run
 set color0=white
 set color1=black
 set xbrushwidth=2
 plot v(in1) v(in2) v(out)
 meas tran tpdr
 + TRIG v(in1) VAL=0.9 FALL=1
 + TARG v(out) VAL=0.9 RISE=1
 meas tran tpdf
 + TRIG v(in1) VAL=0.9 RISE=1
 + TARG v(out) VAL=0.9 FALL=1
.endc
