from sklearn import linear_model
import pandas as pd

def linModel():
    files=["INVx2","INVx4","NAND2x2","NAND3x2","NOR2x2","NOR3x2"]
    types=["tpdf","tpdr"]
    x=0
    y=0
    coef=[]
    for i in files:
        df = pd.read_csv('{}_alldata.csv'.format(i))
        for j in types:
            y=df[j]
            x=df[['CL','Input Transtions']]
            reg=linear_model.LinearRegression()
            reg.fit(x,y)
            coef=reg.coef_
            print(i+"\t"+j)
            print("K1:{}\tK2:{}".format(coef[0],coef[1]))

if __name__== "__main__":
    linModel()