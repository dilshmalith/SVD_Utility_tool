import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import matplotlib.pyplot as plt
from File_handling import variables_selected as VS

class Error:

#mat1 represents the original dataset.
    def __init__(self,mat1=[],mat2=[]):
        self.mat1=mat1
        self.mat2=mat2
        self.rows=np.shape(mat1)[0]
        self.columns=np.shape(mat1)[1]
        self.error=[0 for col in range(self.columns)]
        self.coef=[0 for col in range(self.columns)]
        self.df1=pd.DataFrame(mat1)
        self.df1=pd.DataFrame(mat1)

        self.X =figure_X()
        #self.Configure_X()    #Comment out if X axis needs to be rank



    def RMSE(self):
        for i in range (0,self.columns,1):
            cum=0
            for j in range (0,self.rows,1):
                cum= cum + (self.mat1[j][i]-self.mat2[j][i])**2



            self.error[i]=cum

        for i in range (0,self.columns,1):
            self.error[i]=self.error[i]/self.rows
            self.error[i]=math.sqrt(self.error[i])
            self.error[i]=round(self.error[i],3)
        #print(self.error)  #Print if you need to verify

    def cor_coef(self):

        temp=[0 for col in range(self.columns)]
        from Vgraphs import normalized
        df1=normalized(self.mat1)
        df2=normalized(self.mat2)
        mean1=df1.meancal()
        mean2=df2.meancal()
        stdv1=df1.std_dev()
        stdv2=df2.std_dev()


        for i in range (0,self.columns,1):
            cum=0
            for j in range (0,self.rows,1):
                cum= cum + (self.mat1[j][i]-mean1[i])*(self.mat2[j][i]-mean2[i])


            temp[i]=cum

        for i in range (0,self.columns,1):
            temp[i]=temp[i]/(stdv1[i]*stdv2[i])
            temp[i]=temp[i]/self.rows
            temp[i]=float(temp[i])
            temp[i]=round(temp[i],3)
            self.coef[i]=temp[i]
        #print(self.coef)     #Print if you need to verify

    def RMSE_plot(self):

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.plot(self.X, self.error,'g',linestyle='solid')
        ax.grid(color = 'grey', linestyle = '--', linewidth = 0.3)
        ax.set_title("Root mean Square error")
        ax.set_xlabel("Variable")
        ax.set_ylabel("Error")
        plt.show()

    def cor_coef_plot(self):

        fig2, ax2 = plt.subplots(figsize=(10, 10))
        ax2.plot(self.X,self.coef,'g',linestyle='solid')
        ax2.grid(color = 'grey', linestyle = '--', linewidth = 0.3)
        ax2.set_title("Correlation Coefficient")
        ax2.set_xlabel("Variable")
        ax2.set_ylabel("value")
        plt.show()


    def Configure_X(self):
        x=[]
        if VS[0]==1:
            x.append("Pressure")

        if VS[1]==1:
            x.append("Mag-x")
            x.append("Mag-y")
            x.append("Mag-z")

        if VS[2]==1:
            x.append("Acc-x")
            x.append("Acc-y")
            x.append("Acc-z")

        if VS[3]==1:
            x.append("Qua-a")
            x.append("Qua-b")
            x.append("Qua-c")
            x.append("Qua-d")

        if VS[4]==1:
            x.append("Knee angle")

        for i in range (0, len(x),1):
            self.X.append(x[i])


    def Save_RMSE(self):
        np.savetxt("rmse.csv" ,self.error , delimiter=",", header="Root mean Square Error")

    def Save_cor_coef(self):
        np.savetxt("Correlation_Coefficient.csv" ,self.coef , delimiter=",", header="Correlation Coefficient")

def figure_X():
        x=[]
        if VS[0]==1:
            x.append("Pressure")

        if VS[1]==1:
            x.append("Mag-x")
            x.append("Mag-y")
            x.append("Mag-z")

        if VS[2]==1:
            x.append("Acc-x")
            x.append("Acc-y")
            x.append("Acc-z")

        if VS[3]==1:
            x.append("Qua-a")
            x.append("Qua-b")
            x.append("Qua-c")
            x.append("Qua-d")

        if VS[4]==1:
            x.append("Knee angle")

        return x

