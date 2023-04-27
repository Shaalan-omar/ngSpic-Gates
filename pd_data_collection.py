import pandas as pd
import csv
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()
from PySpice.Spice.NgSpice.Shared import NgSpiceShared
ngspice = NgSpiceShared.new_instance()


def probagartion_data_collection():
    files=["INVx2","INVx4","NAND2x2","NAND3x2","NOR2x2","NOR3x2"]
    loadCaps=["1","3","5","7","9","11","13","15"]
    inputTrans=["0.1","0.25","0.5","0.75","1","1.25","1.5"]
    tpdf=0
    tpdr=0
    temp=0
    tpdf_list=[]
    inptrans=[]
    cl=[]
    tpdr_list=[]
    for i in files:
        for j in loadCaps:
            for k in inputTrans:
                match i:
                    case "INVx2":
                        circuit='''
                        .include .\sky130_fd_pr_ngspice\sky130.sp
                        .subckt INVx2 a b vdd gnd 
                        X1 b a vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
                        X2 b a gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
                        .ends

                        vdd vdd gnd 1.8v
                        vin x gnd PULSE 0 1.8 0ps {}ns {}ns 2.5ns 5ns
                        X1 x y vdd gnd INVx2
                        CL1 y gnd {}fF

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
                        wrdata tpdr_temp.csv tpdr
                        wrdata tpdf_temp.csv tpdf
                        .endc
                        .END
                        '''.format(k,k,j)
                    case "INVx4":
                        circuit='''
                        .include .\sky130_fd_pr_ngspice\sky130.sp
                        .subckt INVx4 a b vdd gnd 
                        X1 b a vdd vdd sky130_fd_pr__pfet_01v8 W=4000000u L=150000u
                        X2 b a gnd gnd sky130_fd_pr__nfet_01v8 W=1680000u L=150000u
                        .ends

                        vdd vdd gnd 1.8v
                        vin x gnd PULSE 0 1.8 0ps {}ns {}ns 2.5ns 5ns
                        X1 x y vdd gnd INVx4
                        CL1 y gnd {}fF

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
                        wrdata tpdr_temp.csv tpdr
                        wrdata tpdf_temp.csv tpdf
                        .endc
                        .END
                        '''.format(k,k,j)
                    case "NAND2x2":
                        circuit='''
                        .include .\sky130_fd_pr_ngspice\sky130.sp
                        .subckt NAND2x2 a b y vdd gnd
                        X1 y a vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u *size of 2
                        X2 y b vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u *size of 2 
                        X3 y a n1 gnd sky130_fd_pr__nfet_01v8 W=1680000u L=150000u *size of 2
                        X4 n1 b gnd gnd sky130_fd_pr__nfet_01v8 W=1680000u L=150000u *size of 2
                        .ends


                        vdd vdd gnd 1.8v
                        vina a gnd PULSE 0 1.8 0ps {}ns {}ns 2.5ns 5ns
                        vinb b gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns


                        X1 a b y vdd gnd NAND2x2
                        CL1 y gnd {}fF

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
                        wrdata tpdr_temp.csv tpdr
                        wrdata tpdf_temp.csv tpdf
                        .endc
                        .END
                        '''.format(k,k,k,k,j)
                    case "NAND3x2":
                        circuit='''
                        .include .\sky130_fd_pr_ngspice\sky130.sp
                        .subckt NAND3x2 a b c y vdd gnd
                        X1 y a vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
                        X2 y b vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
                        X3 y c vdd vdd sky130_fd_pr__pfet_01v8 W=2000000u L=150000u
                        X4 y a f f sky130_fd_pr__nfet_01v8 W=3000000u L=150000u
                        X5 f b g g sky130_fd_pr__nfet_01v8 W=3000000u L=150000u
                        X6 g c gnd gnd sky130_fd_pr__nfet_01v8 W=3000000u L=150000u
                        .ends
                        vdd vdd gnd 1.8v
                        vina a gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns
                        vinb b gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns
                        vinc c gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns

                        X1 a b c y vdd gnd NAND3x2
                        CL1 y gnd {}fF

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
                        wrdata tpdr_temp.csv tpdr
                        wrdata tpdf_temp.csv tpdf
                        .endc
                        .END
                        '''.format(k,k,k,k,k,k,j)
                    case "NOR2x2":
                        circuit='''
                        .include .\sky130_fd_pr_ngspice\sky130.sp
                        .subckt Nor2x2 in1 in2 out vdd gnd
                        X1 w1 in1 vdd vdd sky130_fd_pr__pfet_01v8 W=4000000u L=150000u 
                        X2 out in2 w1 w1 sky130_fd_pr__pfet_01v8 W=4000000u L=150000u 
                        X3 out in1 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
                        X4 out in2 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
                        .ends

                        vdd vdd gnd 1.8v
                        vinin1 in1 gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns
                        vinin2 in2 gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns

                        X1 in1 in2 out vdd gnd Nor2x2
                        CL1 out gnd {}fF

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
                        wrdata tpdr_temp.csv tpdr
                        wrdata tpdf_temp.csv tpdf
                        .endc
                        .END
                        '''.format(k,k,k,k,j)
                    case "NOR3x2":
                        circuit='''
                        .include .\sky130_fd_pr_ngspice\sky130.sp
                        .subckt Nor3x2 in1 in2 in3 out vdd gnd
                        X1 w1 in1 vdd vdd sky130_fd_pr__pfet_01v8 W=7000000u L=150000u 
                        X2 w2 in2 w1 w1 sky130_fd_pr__pfet_01v8 W=7000000u L=150000u 
                        X3 out in3 w2 w2 sky130_fd_pr__pfet_01v8 W=7000000u L=150000u 

                        X4 out in1 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
                        X5 out in2 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
                        X6 out in3 gnd gnd sky130_fd_pr__nfet_01v8 W=840000u L=150000u
                        .ends

                        vdd vdd gnd 1.8v
                        vinin1 in1 gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns
                        vinin2 in2 gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns
                        vinin3 in3 gnd PULSE 0 1.8 0ps {}ns {}ns 5ns 10ns
                        X1 in1 in2 in3 out vdd gnd Nor3x2
                        CL1 out gnd {}fF

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
                        wrdata tpdr_temp.csv tpdr
                        wrdata tpdf_temp.csv tpdf
                        .endc
                        .END
                        '''.format(k,k,k,k,k,k,j)
                ngspice.load_circuit(circuit)
                ngspice.run()
                with open('tpdf_temp.csv','r') as temp1:
                    reader=csv.reader(temp1)
                    row1=next(reader)
                    temp = row1[0].split()
                    tpdf=temp[1]
                    tpdf_list.append(tpdf)
                with open('tpdr_temp.csv','r') as temp1:
                    reader=csv.reader(temp1)
                    row1=next(reader)
                    temp = row1[0].split()
                    tpdr=temp[1]
                    tpdr_list.append(tpdr)
                cl.append(j)
                inptrans.append(k)
        df_alldata=pd.DataFrame({'CL':cl,'Input Transtions':inptrans,'tpdf':tpdf_list,'tpdr':tpdr_list})
        df_alldata.to_csv('{}_alldata.csv'.format(i),index=False,header=True)
        tpdf_list[:]=[]
        tpdr_list[:]=[]
        cl[:]=[]
        inptrans[:]=[]

if __name__ == "__main__":
    probagartion_data_collection()