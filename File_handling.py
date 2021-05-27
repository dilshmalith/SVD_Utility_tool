
#Tkinter GUI module
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import numpy as  np
import sys
import pandas as pd
import time
import os

#Global variables
global_filecount=0
multi_array=[]
rows_final=0
columns_final=0
in_array=[]
sts_selected=0
columns_selected=[]
variables_selected=[]   #Binary representation of selected variables. Order of the variables to be maintained
pressure=0   #Initiaize
acceleration=0  #Initialize
magnetic_field=0   #Initialize
quaternions=0       #Initialize
Knee_angle=0           #Initialize
all_variables=5 #If more variables are added change the value here. This value does not include 'All' option
sub_rate=0
int_subrate=0
Normalization=0  #
path=os.getcwd()  #Current directory


#Define GUI window 1
fopen_window=tk.Tk()
frame1=tk.Frame(fopen_window)
frame1.pack()
fopen_window.title("File Selection")
fopen_window.geometry('300x300')
fopen_window.iconbitmap(path+'/icon.ico')

#Defining command function for single_button
def read_single_file():
  file_open=filedialog.askopenfile(mode="r",title="File Selection",filetypes=[("Text files", "*.txt")])
  #print(file_open.name)
  single_file=open(file_open.name, "r")
  single_data=single_file.read()
  single_data=single_data.split()
  Slength=len(single_data)
  Scolumns=15
  Srows=int(Slength/Scolumns)
  global in_array
  in_array= [[0 for col in range(Scolumns)] for col in range(Srows)]
  for i in range(0,Srows,1):
    for j in range(0,Scolumns,1):
      z=15*i+j
      in_array[i][j]=single_data[z]

  global columns_final
  columns_final=Scolumns
  global rows_final
  rows_final=Srows
  global global_filecount
  global_filecount=1

  global sts_selected
  if global_filecount==1:
    sts_selected=1
  exit=fopen_window.destroy()


    #Defining command function for multi_button
def read_multiple_files():
  file_open=filedialog.askopenfiles(mode="r",title="File Selection",filetypes=[("Text files", "*.txt")])
  number_of_files=len(file_open) #Count the number of files selected by the user

   #Define arrays to buffer the data input and to track the length of each array
  multi_data=[0 for i in range(number_of_files)]
  len_data=[0 for i in range(number_of_files)]
  rows_data=[0 for i in range(number_of_files)]

  for i in range(0,number_of_files,1):
   #print(file_open[i].name)           #To print file names
   multi_mine=open(file_open[i].name, "r")
   multi_data[i]=multi_mine.read() #Reads each file in the loop as a 'string'
   multi_data[i]=multi_data[i].split() #Separates each value and creates a 2D array
   len_data[i]=len(multi_data[i])
   rows_data[i]=int(len_data[i]/15)



  Mcolumns2=15
  Mrows2=int(sum(len_data)/Mcolumns2)

  cum_len=np.cumsum(len_data)
  global in_array
  in_array= [[0 for col in range(Mcolumns2)] for col in range(Mrows2)]
  loop_count =0
  for i in range(0,number_of_files,1):
    for j in range(0,rows_data[i],1):
      for k in range(0,Mcolumns2,1):
        z=15*j+k
        in_array[loop_count][k]=multi_data[i][z]

      loop_count=loop_count+1

  global global_filecount
  global_filecount=number_of_files
  global columns_final
  columns_final=Mcolumns2
  global rows_final
  rows_final=Mrows2
  global sts_selected
  if global_filecount>0:
    sts_selected=1
  exit=fopen_window.destroy()

#Define text box
textbox1=tk.Text(frame1,width=32, height=1, bg='grey')
textbox1.pack()
textbox1.insert(tk.END,"Please select the upload option")

label1=tk.Label(frame1,text="Click the button to continue")
label1.pack(pady=20)

#create a button for reading  from a single file
single_button = tk.Button(frame1,height=2, width=10, text="Single file", bg="light Blue",fg="Black",command=read_single_file)
single_button.pack(side=tk.LEFT)

#create a button for reading from multiple files
multi_button = tk.Button(frame1, height=2, width=10, text="Multiple Files",bg="Light Blue", fg="Black",command=read_multiple_files)
multi_button.pack(side=tk.RIGHT)

def shutdown():
     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
       exit()

fopen_window.protocol("WM_DELETE_WINDOW", shutdown)

fopen_window.mainloop()



if sts_selected==1:



  #Tkinter GUI for Column selection
 Column_selection=tk.Tk()
 frame2=tk.Frame(Column_selection)
 frame2.pack()
 Column_selection.title("Variable selection")
 Column_selection.geometry('350x350')
 Column_selection.iconbitmap(path+'/icon.ico')

 textbox2=tk.Text(frame2,width=30, height=1, bg='grey', bd=4)
 textbox2.pack()
 textbox2.insert(tk.END,"Select variables")

 Listbox1=tk.Listbox(frame2,height=10, selectmode='multiple', cursor='arrow')
 Listbox1.pack(pady=10)
 Listbox1.insert(0,"Pressure")
 Listbox1.insert(1,"Acceleration")
 Listbox1.insert(2,"Magnetic Field")
 Listbox1.insert(3,"Quaternions")
 Listbox1.insert(4,"Knee angle")
 Listbox1.insert(5,"All")



 def confirm_variants():
   global columns_selected
   for i in Listbox1.curselection():
     columns_selected.append(Listbox1.get(i))

   Column_selection.destroy()

 confirm_button = tk.Button(frame2, text="Confirm", bg="green",fg="Black",command=confirm_variants)
 confirm_button.pack(pady=10)

 def shutdown():
     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
       exit()

 Column_selection.protocol("WM_DELETE_WINDOW", shutdown)

 Column_selection.mainloop()
  
#Program exits if no variable selection is made
 if len(columns_selected)==0:
     exit()

 Samplerate_selection=tk.Tk()
 frame3=tk.Frame(Samplerate_selection)
 frame3.pack()
 Samplerate_selection.title("Sample rate")
 Samplerate_selection.geometry('300x300')
 Samplerate_selection.iconbitmap(path+'/icon.ico')

 textbox3=tk.Text(frame3,width=25, height=1, bg='Grey', bd=4)
 textbox3.pack(side=tk.TOP)
 #textbox3.place(x=30,y=5)
 textbox3.insert(tk.END,"Enter Sub Sampling rate")

 sampling_label=tk.Label(frame3, text="Enter a value between 1-10")
 sampling_label.pack(pady=10)

 entry=tk.Entry(frame3,width=5)
 entry.pack(side=tk.TOP)

 def confirm_normalization():

     global Normalization

     answer=messagebox.askyesno("Normalization confirm", "Do you really want to use normalized data?")

     if answer:
         Normalization=1
         normalizing_label=tk.Label(frame3, text="Normalization data added to the analysis")
         normalizing_label.pack()

 Normalization_button=tk.Button(frame3, text="Use Normalized data", bg="grey",fg="Black",command=confirm_normalization)
 Normalization_button.pack(pady=10)

 def confirm_sampling_rate():
    global sub_rate
    global int_subrate

    sub_rate=entry.get()
    #sub_rate=int(sub_rate)
    try:
        int_subrate=int(sub_rate)


        if (1<=int_subrate) and (int_subrate<=10) :
           Samplerate_selection.destroy()

        else:
           wrong_input=tk.Tk()
           frame4=tk.Frame(wrong_input)
           frame4.pack()
           wrong_input.title("Error!")
           wrong_input.iconbitmap(path+'/icon.ico')
           Samplerate_selection.geometry('100x40')

           textbox4=tk.Text(frame4,width=25, height=1, bd=4)
           textbox4.pack(pady=10)
           textbox4.insert(tk.END,"Input out of range")
           wrong_input.after(2000, lambda:wrong_input.destroy())
           Samplerate_selection.after(3000, lambda:Samplerate_selection.destroy())
           wrong_input.mainloop()
           Samplerate_selection.mainloop()
           exit()


    except ValueError:
      wrong_input=tk.Tk()
      frame4=tk.Frame(wrong_input)
      frame4.pack()
      wrong_input.title("Error!")
      wrong_input.iconbitmap(path+'/icon.ico')
      Samplerate_selection.geometry('100x40')

      textbox4=tk.Text(frame4,width=25, height=1, bd=4)
      textbox4.pack(pady=10)
      textbox4.insert(tk.END,"Not an integer")

      wrong_input.after(2000, lambda:wrong_input.destroy())
      Samplerate_selection.after(3000, lambda:Samplerate_selection.destroy())
      wrong_input.mainloop()
      Samplerate_selection.mainloop()
      exit()


 def shutdown():
     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
       exit()

 Samplerate_selection.protocol("WM_DELETE_WINDOW", shutdown)


 confirm_button2 = tk.Button(frame3, text="Confirm", bg="green",fg="Black",command=confirm_sampling_rate)
 confirm_button2.pack(side=tk.BOTTOM,pady=10)



 Samplerate_selection.mainloop()

else:

 sys.exit("An error has occurred")

variables_selected=[0 for i in range(all_variables)]

pd_array=pd.DataFrame(in_array, columns=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14','col15'])

pd_array.drop(columns=['col1','col3','col4'],axis=1, inplace=True)


#Applying sub sampling rate for reducing rows
if (1<=int_subrate) and (int_subrate<=10):
    for i in range(0,rows_final-1,1):
      p=(i+1)%int_subrate
      if (p!=0):
            pd_array.drop(index=[i+1],axis=0, inplace=True)



for i in range(len(columns_selected)):
    if (columns_selected[i]=='Acceleration') or (columns_selected[i]=='All'):
        acceleration=1
        variables_selected[2]=1


if not acceleration==1:
     pd_array.drop(columns=['col8','col9','col10'],axis=1,inplace=True)


for i in range(len(columns_selected)):
    if (columns_selected[i]=='Magnetic Field' or columns_selected[i]=='All'):
        magnetic_field=1
        variables_selected[1]=1

if not magnetic_field==1:
        pd_array.drop(columns=['col5','col6','col7'],inplace=True)

for i in range(len(columns_selected)):
    if (columns_selected[i]=='Quaternions' or columns_selected[i]=='All'):
        quaternions=1
        variables_selected[3]=1

if not quaternions==1:
        pd_array.drop(columns=['col11','col12','col13','col14'],inplace=True)

for i in range(len(columns_selected)):
    if (columns_selected[i]=='Pressure' or columns_selected[i]=='All'):
        pressure=1
        variables_selected[0]=1

if not pressure==1:
        pd_array.drop(columns=['col2'],inplace=True)

for i in range(len(columns_selected)):
    if (columns_selected[i]=='Knee angle' or columns_selected[i]=='All'):
        Knee_angle=1
        variables_selected[4]=1

if not Knee_angle==1:
        pd_array.drop(columns=['col15'],inplace=True)

final_array=pd_array.to_numpy()

input_rows=np.shape(final_array)[0]
input_columns=np.shape(final_array)[1]

svd_in=[[0 for col in range(input_columns)] for col in range(input_rows)]

for i in range(0,input_rows,1):
    for j in range(0,input_columns,1):
      svd_in[i][j]=float(final_array[i][j])










