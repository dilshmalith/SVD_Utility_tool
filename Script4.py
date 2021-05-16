
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Script1 import variables_selected as VS
from Script8 import figure_X

#Global variables

class normalized:


    def __init__(self,inp_data=[]):
        self.inp_data=inp_data
        self.rows=np.shape(self.inp_data)[0]
        self.columns=np.shape(self.inp_data)[1]
        self.dataframe=pd.DataFrame(self.inp_data)


    def meancal(self):
        self.mean=self.dataframe.mean(axis=0)
        return self.mean

    def std_dev(self):
        self.std=self.dataframe.std(axis=0)
        return self.std

    def nrm_out(self):
        self.meancal()
        self.std_dev()
        output=[[0 for col in range(self.columns)] for col in range(self.rows)]
        for i in range(0,self.rows,1):
          for j in range(0,self.columns,1):
              output[i][j]=(self.inp_data[i][j]-self.mean[j])/self.std[j]
              output[i][j]=float(output[i][j])

        return output



class V_plots:
     def __init__(self,inp_data=[]):
        self.inp_data=inp_data
        self.rows=np.shape(self.inp_data)[0]
        self.columns=np.shape(self.inp_data)[1]
        self.transposed=np.transpose(self.inp_data)
        self.dataframe=pd.DataFrame(self.transposed)

     def x_range(self):
         time=np.linspace(1, self.rows, num=self.rows)
         return(time)

     def plot(self):
         legend=[]
         x_range=self.x_range()
         fig, ax = plt.subplots(figsize=(10, 10))
         ax.set_title("V' modes")
         ax.set_xlabel("Rank")
         ax.set_ylabel("Contribution")
         for i in range(0,self.columns,1):

            ax.plot(x_range,self.dataframe[i])
            
         ax.xaxis.set_ticks(np.arange(min(x_range),max(x_range)+1 ,1))
         legend=figure_X()
         plt.figlegend(legend)
         plt.show()

