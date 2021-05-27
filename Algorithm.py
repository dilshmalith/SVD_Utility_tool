from File_handling import svd_in
from File_handling import Normalization
from tkinter import messagebox
from Vgraphs import normalized
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import tkinter as tk
import time
import pandas as pd

#Global variables
inp_rank=0
path=os.getcwd()  #Current directory



nrm_object=normalized(svd_in)   #Creating an instance of the class :normalized
nrm_matrix=nrm_object.nrm_out()  #Normalized data output assigned to a new variable

#Logic decides which matrix to proceed based on user input
if Normalization==1:
    svd_matrix=nrm_matrix

else:
    svd_matrix=svd_in

#SVD calculation
U, S, V = np.linalg.svd(svd_matrix)

"""
print("\n \n U matrix is")
print(U)
print("\n \n Sigma matrix is")
print(S)
print("\n \n V matrix is")
print(V)
print("\n \n Nomalization active or not")
print(Normalization)
"""


t_rank=len(S)

if t_rank>1 :
 rank_selection=tk.Tk()
 frame5=tk.Frame(rank_selection)
 frame5.pack()
 rank_selection.title("Rank Selection")
 rank_selection.geometry('300x300')
 rank_selection.iconbitmap(path+'/icon.ico')

 textbox5=tk.Text(frame5,width=25, height=1, bg='Grey', bd=4)
 textbox5.pack(pady=10)
 textbox5.insert(tk.END,"Enter rank selection")

 entry=tk.Entry(frame5,width=5)
 entry.pack(pady=15)


 rank_label=tk.Label(frame5, text=f"Enter a value between 1 and {t_rank}")
 rank_label.pack()

 textbox_g=tk.Text(frame5,width=25, height=1, bg='Grey', bd=4)
 textbox_g.pack(pady=10)
 textbox_g.insert(tk.END,"Basic SVD graphs")

 def open_svdPlot():
    from Rank_graphs import SVD_plots
    #Creating an object from the class :SVD_plots  xxxxxx Plots Rank vs S
    svdobj=SVD_plots(S)
    svdobj.userplot()

 svd_plot_button=tk.Button(frame5, text="S vs Rank", bg="light Grey",fg="Black",command=open_svdPlot)
 svd_plot_button.pack()

 def open_vplot_command():
     from Vgraphs import V_plots
     V_newplot=V_plots(V)
     V_newplot.plot()


 V_plot_button=tk.Button(frame5, text="V' Plot", bg="light Grey",fg="Black",command=open_vplot_command)
 V_plot_button.pack()

#2021-05-12
 #Custom built Saving function is inhibited due to the built in "save as" function in the matplotlib

 """
 def save_vplot_command():
    from Rank_graphs import SVD_plots
    #Creating an object from the class :SVD_plots  xxxxxx Plots Rank vs S
    svdobj2=SVD_plots(S)
    svdobj2.userplot(id=1)


 save_plot_button=tk.Button(frame5, text="Save plot", bg="light Grey",fg="Black",command=save_vplot_command)
 save_plot_button.pack()
 
 """

 def confirm_rank():
    global inp_rank


    inp_rank=entry.get()

    try:
        inp_rank=int(inp_rank)


        if (1<=inp_rank) and (inp_rank<=t_rank) :
           rank_selection.destroy()

        else:
           wrong_input=tk.Tk()
           frame6=tk.Frame(wrong_input)
           frame6.pack()
           wrong_input.title("Error!")
           wrong_input.geometry('200x60')
           wrong_input.iconbitmap(path+'/icon.ico')

           textbox6=tk.Text(frame6,width=25, height=1, bd=4)
           textbox6.pack(pady=10)
           textbox6.insert(tk.END,"Input out of range")
           wrong_input.after(2000, lambda:wrong_input.destroy())
           rank_selection.after(3000, lambda:rank_selection.destroy())
           wrong_input.mainloop()
           rank_selection.mainloop()
           exit()


    except ValueError:
      wrong_input=tk.Tk()
      frame6=tk.Frame(wrong_input)
      frame6.pack()
      wrong_input.title("Error!")
      wrong_input.geometry('200x60')
      wrong_input.iconbitmap(path+'/icon.ico')

      textbox4=tk.Text(frame6,width=25, height=1, bd=4)
      textbox4.pack(pady=10)
      textbox4.insert(tk.END,"Not an integer")

      wrong_input.after(2000, lambda:wrong_input.destroy())
      rank_selection.after(3000, lambda:rank_selection.destroy())
      wrong_input.mainloop()
      rank_selection.mainloop()
      exit()


 confirm_button3 = tk.Button(frame5, text="Confirm", bg="green",fg="Black",command=confirm_rank)
 confirm_button3.pack(pady=20)

 def confirm_home():
     rank_selection.destroy()
     import Reboot

 HomeButoon = tk.Button(frame5, text="Home", bg="grey",fg="Black",command=confirm_home)
 HomeButoon.pack()

 def shutdown():
     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
       exit()

 rank_selection.protocol("WM_DELETE_WINDOW", shutdown)

 rank_selection.mainloop()

elif t_rank==1:
    inp_rank=1

"""
print("Dimensions U")
print(np.shape(U))
print("Dimensions V")
print(np.shape(V))
print("Dimensions S")
print(np.shape(S))
"""

Rec_Srows=np.shape(U)[0]
Rec_Scolmuns=np.shape(V)[1]

Rec_S=[[0 for i in range(Rec_Scolmuns)] for j in range(Rec_Srows)]

Var_S=[[0 for i in range(Rec_Scolmuns)] for j in range(Rec_Srows)]

Rec_SVD=[[0 for i in range(Rec_Scolmuns)] for j in range(Rec_Srows)]


#Var_S[:inp_rank, :inp_rank] = np.diag(S)

for i in range(0,inp_rank,1):
    Rec_S[i][i]=S[i]

#Row rank approimation
Rec_SVD=U @ (Rec_S @ V)
comparison=np.allclose(svd_matrix,Rec_SVD)


Tolerence=[[0 for i in range(Rec_Scolmuns)] for j in range(Rec_Srows)]
Tolerence=abs(svd_matrix-Rec_SVD)



for i in range (0,Rec_Srows,1):
    for j in range (0,Rec_Scolmuns,1):
        Tolerence[i][j]=float(Tolerence[i][j])
        Tolerence[i][j]=abs(Tolerence[i][j]/svd_matrix[i][j]* 100)




file_rec = open("file_rec.txt", "w")
np.savetxt("file_rec.txt" ,Rec_SVD , delimiter=",")
#file_rec.write("Your text goes here")
file_rec.close()











