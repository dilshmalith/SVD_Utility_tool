from Script2 import Rec_SVD
from Script1 import variables_selected as VS
from Script2 import svd_matrix as S_in
from Script2 import V
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from Script4 import normalized
from Script8 import Error
import os


#Global variables
X1=[]
X2=[]
time=0
path=os.getcwd()  #Current directory

length=np.shape(S_in)[0]
X1=pd.DataFrame(S_in)
X2=pd.DataFrame(Rec_SVD)
time=np.arange(length)

#Creating a Tkinter GUI window
graph_selection=tk.Tk()
frame10=tk.Frame(graph_selection)
frame10.pack()
graph_selection.title("Rank Approximation Graphs")
graph_selection.geometry('350x300')
graph_selection.iconbitmap(path+'/icon.ico')

textbox10=tk.Text(frame10,width=25, height=1, bg='Grey', bd=4)
textbox10.pack(pady=10)
textbox10.insert(tk.END,"Select the variable")

#Control function for Pressure graph
def open_pressure():
    global time
    global X1
    global X2
    if VS[0]==1:
        plt.plot(time,X1[0],'g')
        plt.plot(time,X2[0],'r',linestyle='--')
        plt.xlabel("Time (x 10ms)")
        plt.ylabel("Pressure (mBar)")
        plt.title("Input Pressure vs Recreated Pressure")
        plt.legend(["Original", "Reconstructed"])
        plt.show()
    else:
        wrong_input=tk.Tk()
        frame11=tk.Frame(wrong_input)
        frame11.pack()
        wrong_input.title("Error!")
        wrong_input.geometry('200x60')
        wrong_input.iconbitmap(path+'/icon.ico')

        textbox11=tk.Text(frame11,width=25, height=1, bd=4)
        textbox11.pack(pady=10)
        textbox11.insert(tk.END,"Variable Not Available")

        wrong_input.after(2000, lambda:wrong_input.destroy())
        wrong_input.mainloop()

#Createing a button for pressure
pressure = tk.Button(frame10, text="Pressure", bg="light grey",fg="Black",command=open_pressure,height=1, width=12)
pressure.pack(pady=5,side = tk.TOP)


#Control function for Knee angle
def open_Knee_angle():
    global time
    global X1
    global X2
    w=0
    if VS[4]==1:

        if VS[0]==1:
            w=w+1

        if VS[1]==1:
            w=w+3

        if VS[2]==1:
            w=w+3

        if VS[3]==1:
            w=w+4

        plt.plot(time,X1[w],'g')
        plt.plot(time,X2[w],'r',linestyle='--')
        plt.xlabel("Time (x 10ms)")
        plt.ylabel("Knee angle")
        plt.title("Input Knee angle vs Approximated Knee angle")
        plt.legend(["Original", "Reconstructed"])
        plt.show()
    else:
        wrong_input=tk.Tk()
        frame11=tk.Frame(wrong_input)
        frame11.pack()
        wrong_input.title("Error!")
        wrong_input.geometry('200x60')
        wrong_input.iconbitmap(path+'/icon.ico')

        textbox11=tk.Text(frame11,width=25, height=1, bd=4)
        textbox11.pack(pady=10)
        textbox11.insert(tk.END,"Variable Not Available")

        wrong_input.after(2000, lambda:wrong_input.destroy())
        wrong_input.mainloop()

#Createing a button for pressure
Knee_angle = tk.Button(frame10, text="Knee angle", bg="light grey",fg="Black",command=open_Knee_angle, height=1, width=12)
Knee_angle.pack(pady=5,side=tk.TOP)


#Control function for acceleration graph
def open_acceleration():
    global time
    global X1
    global X2
    w=0
    if VS[2]==1:
        if VS[0]==1:
            w=1

        if VS[1]==1:
            w=w+3

        fig, ax = plt.subplots(3,figsize=(10, 10) )

        ax[0].set_title('Input Acceleration-x vs Approximated Acceleration-x')
        ax[0].set_xlabel('Time (x 10ms)')
        ax[0].set_ylabel('Acceleration-x (ms-2)')
        ax[0].plot(time,X1[w],'g',linestyle='solid')
        ax[0].plot(time,X2[w],'r',linestyle='--')
        plt.legend(["x-Original", "x-Reconstructed"])

        plt.tight_layout(pad=3)

        ax[1].set_title('Input Acceleration-y vs Approximated Acceleration-y')
        ax[1].set_xlabel('Time (x 10ms)')
        ax[1].set_ylabel('Acceleration-y (ms-2)')
        ax[1].plot(time,X1[w+1],'g',linestyle='solid')
        #ax[1].plot(time,X1[2],'b',linestyle='solid')
        ax[1].plot(time,X2[w+1],'r',linestyle='--')
        #plt.legend(["Original", "Reconstructed"])

        plt.tight_layout(pad=3)

        ax[2].set_title('Input Acceleration-z vs Approximated Acceleration-z')
        ax[2].set_xlabel('Time (x 10ms)')
        ax[2].set_ylabel('Acceleration-z (ms-2)')
        ax[2].plot(time,X1[w+2],'g',linestyle='solid')
        ax[2].plot(time,X2[w+2],'r',linestyle='--')
        plt.figlegend(('x-org','x-rec','y-org','y-rec','z-org','z-rec'))

        plt.show()
    else:
        wrong_input=tk.Tk()
        frame11=tk.Frame(wrong_input)
        frame11.pack()
        wrong_input.title("Error!")
        wrong_input.geometry('200x60')
        wrong_input.iconbitmap(path+'/icon.ico')

        textbox11=tk.Text(frame11,width=25, height=1, bd=4)
        textbox11.pack(pady=10)
        textbox11.insert(tk.END,"Variable Not Available")

        wrong_input.after(2000, lambda:wrong_input.destroy())
        wrong_input.mainloop()

#Createing a button for acceleration
acceleration = tk.Button(frame10, text="Acceleration", bg="light grey",fg="Black",command=open_acceleration,height=1, width=12)
acceleration.pack(pady=5,side = tk.TOP)



#Control function for magnetic field
def open_magnetic():
    global time
    global X1
    global X2
    w=0
    if VS[1]==1:
        if VS[0]==1:
            w=w+1

        fig, ax = plt.subplots(3,figsize=(10, 10) )

        ax[0].set_title('Input magnetic field-x vs Approximated magnetic field-x')
        ax[0].set_xlabel('Time (x 10ms)')
        ax[0].set_ylabel('magnetic filed-x (μT)')
        ax[0].plot(time,X1[w],'g',linestyle='solid')
        ax[0].plot(time,X2[w],'r',linestyle='--')
        plt.legend(["x-Original", "x-Reconstructed"])

        plt.tight_layout(pad=3)

        ax[1].set_title('Input magnetic field-y vs Approximated magnetic field-y')
        ax[1].set_xlabel('Time (x 10ms)')
        ax[1].set_ylabel('magnetic filed-y (μT)')
        ax[1].plot(time,X1[w+1],'g',linestyle='solid')
        #ax[1].plot(time,X1[2],'b',linestyle='solid')
        ax[1].plot(time,X2[w+1],'r',linestyle='--')
        #plt.legend(["Original", "Reconstructed"])

        plt.tight_layout(pad=3)

        ax[2].set_title('Input magnetic_field -z vs Approximated magnetic_field -z')
        ax[2].set_xlabel('Time (x 10ms)')
        ax[2].set_ylabel('magnetic_field -z (μT)')
        ax[2].plot(time,X1[w+2],'g',linestyle='solid')
        ax[2].plot(time,X2[w+2],'r',linestyle='--')
        plt.figlegend(('x-org','x-rec','y-org','y-rec','z-org','z-rec'))
        plt.show()
    else:
        wrong_input=tk.Tk()
        frame11=tk.Frame(wrong_input)
        frame11.pack()
        wrong_input.title("Error!")
        wrong_input.geometry('200x60')
        wrong_input.iconbitmap(path+'/icon.ico')

        textbox11=tk.Text(frame11,width=25, height=1, bd=4)
        textbox11.pack(pady=10)
        textbox11.insert(tk.END,"Variable Not Available")

        wrong_input.after(2000, lambda:wrong_input.destroy())
        wrong_input.mainloop()

#Createing a button for magnetic field
magnetic_field = tk.Button(frame10, text="Magnetic_field ", bg="light grey",fg="Black",command=open_magnetic, height=1, width=12)
magnetic_field.pack(pady=5,side = tk.TOP)


#Control function for Quaternions
def open_quaternion():
    global time
    global X1
    global X2
    w=0
    if VS[3]==1:

        if VS[0]==1:
            w=w+1

        if VS[1]==1:
            w=w+3

        if VS[2]==1:
            w=w+3

        fig, ax = plt.subplots(4,figsize=(10, 10) )

        ax[0].set_title('Input quaternion-1 vs Approximated quaternion-1')
        ax[0].set_xlabel('Time (x 10ms)')
        ax[0].set_ylabel('quaternion-1')
        ax[0].plot(time,X1[w],'g',linestyle='solid')
        ax[0].plot(time,X2[w],'r',linestyle='--')
        #plt.legend(["Original", "Reconstructed"])

        plt.tight_layout(pad=3)

        ax[1].set_title('Input quaternion-2 vs Approximated quaternion-2')
        ax[1].set_xlabel('Time (x 10ms)')
        ax[1].set_ylabel('quaternion-2')
        ax[1].plot(time,X1[w+1],'g',linestyle='solid')
        #ax[1].plot(time,X1[2],'b',linestyle='solid')
        ax[1].plot(time,X2[w+1],'r',linestyle='--')
        #plt.legend(["Original", "Reconstructed"])

        plt.tight_layout(pad=3)

        ax[2].set_title('Input quaternion-3 vs Approximated quaternion-3')
        ax[2].set_xlabel('Time (x 10ms)')
        ax[2].set_ylabel('quaternion-3')
        ax[2].plot(time,X1[w+2],'g',linestyle='solid')
        ax[2].plot(time,X2[w+2],'r',linestyle='--')
        #plt.legend(["Original", "Reconstructed"])

        plt.tight_layout(pad=3)

        ax[3].set_title('Input quaternion-4 vs Approximated quaternion-4')
        ax[3].set_xlabel('Time (x 10ms)')
        ax[3].set_ylabel('quaternion-4')
        ax[3].plot(time,X1[w+3],'g',linestyle='solid')
        ax[3].plot(time,X2[w+3],'r',linestyle='--')
        plt.figlegend(('1-org','1-rec','2-org','2-rec','3-org','3-rec','4-org','4-rec'))

        plt.show()
    else:
        wrong_input=tk.Tk()
        frame11=tk.Frame(wrong_input)
        frame11.pack()
        wrong_input.title("Error!")
        wrong_input.geometry('200x60')
        wrong_input.iconbitmap(path+'/icon.ico')

        textbox11=tk.Text(frame11,width=25, height=1, bd=4)
        textbox11.pack(pady=10)
        textbox11.insert(tk.END,"Variable Not Available")

        wrong_input.after(2000, lambda:wrong_input.destroy())
        wrong_input.mainloop()

#Createing a button for magnetic field
quaternion=tk.Button(frame10, text="Quaternion", bg="light grey",fg="Black",command=open_quaternion, height=1, width=12)
quaternion.pack(pady=5, side = tk.TOP)


def open_error():

    feature_selection=tk.Tk()
    frame12=tk.Frame(feature_selection)
    frame12.pack()
    feature_selection.title("Data validation")
    feature_selection.geometry('350x300')
    feature_selection.iconbitmap(path+'/icon.ico')

    textbox12=tk.Text(frame12,width=25, height=1, bg='Grey', bd=4)
    textbox12.pack(pady=5)
    textbox12.insert(tk.END,"Select the Option")

    textbox13=tk.Text(frame12,width=25, height=1, bg='white', bd=4)
    textbox13.pack(pady=10)
    textbox13.insert(tk.END,"Root Mean Square error")



    def RMSEerror_cal_command():
        Error1= Error(S_in, Rec_SVD)
        Error1.RMSE()
        Error1.Save_RMSE()

    RMSEerror_cal=tk.Button(frame12, text="Calculate", bg="grey",fg="Black",command=RMSEerror_cal_command, height=1, width=8)
    RMSEerror_cal.pack(pady=5)

    def RMSEerror_plot_command():
         Error1= Error(S_in, Rec_SVD)
         Error1.RMSE()
         Error1.RMSE_plot()

    RMSEerror_plot=tk.Button(frame12, text="Graph", bg="grey",fg="Black",command=RMSEerror_plot_command, height=1, width=8)
    RMSEerror_plot.pack(pady=5)

    textbox14=tk.Text(frame12,width=25, height=1, bg='white', bd=4)
    textbox14.pack(pady=10)
    textbox14.insert(tk.END,"Correlation Coefficient")

    def Corcof_cal_command():
         Error1= Error(S_in, Rec_SVD)
         Error1.cor_coef()
         Error1.Save_cor_coef()



    Corcof_cal=tk.Button(frame12, text="Calculate", bg="grey",fg="Black",command=Corcof_cal_command, height=1, width=8)
    Corcof_cal.pack(pady=5)

    def Corcof_plot_command():
         Error1= Error(S_in, Rec_SVD)
         Error1.cor_coef()
         Error1.cor_coef_plot()

    Corcof_plot=tk.Button(frame12, text="Graph", bg="grey",fg="Black",command=Corcof_plot_command, height=1, width=8)
    Corcof_plot.pack(pady=5)


features_button=tk.Button(frame10, text="Validation", bg="grey",fg="Black",command=open_error, height=1, width=8)
features_button.pack(padx=30,pady=10, side=tk.LEFT)

def confirm_home():
     graph_selection.destroy()
     import Script6

HomeButoon = tk.Button(frame10, text="Home", bg="grey",fg="Black",command=confirm_home)
HomeButoon.pack(side=tk.LEFT)

graph_selection.mainloop()
