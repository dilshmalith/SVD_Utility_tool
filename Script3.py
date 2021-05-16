import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
from tkinter import messagebox

class SVD_plots:
    fig, ax = plt.subplots(3,figsize=(10, 10) )
    confirm_save=0

    def __init__(self,inp_data=[]):
        self.inp_data=inp_data
        self.length=len(inp_data)
        self.id=id

        self.xaxis_points=[0 for i in range(self.length)]
        self.S_log=[0 for i in range(self.length)]
        self.S_cum=[0 for i in range(self.length)]

        self.inp_data=np.array(self.inp_data)
        for i in range (0,self.length,1):
          self.xaxis_points[i]=i+1
          self.S_log[i]=np.log(self.inp_data[i]) #Natural log calculator
        self.S_cum=np.cumsum(self.inp_data,dtype=float)
        total=self.S_cum[-1]
        """
        for i in range (0,self.length,1):
           self.S_cum[i]= self.S_cum[i]/total
            """

#Plot1 Sigma vs rank
    def plot1(self):

       SVD_plots.ax[0].set_title('Sigma vs rank')
       SVD_plots.ax[0].set_xlabel('Rank')
       SVD_plots.ax[0].set_ylabel('Sigma')
       SVD_plots.ax[0].grid(color = 'grey', linestyle = '--', linewidth = 0.3)
       SVD_plots.ax[0].xaxis.set_ticks(np.arange(min(self.xaxis_points),max(self.xaxis_points)+1 ,1))
       SVD_plots.ax[0].plot(self.xaxis_points,self.inp_data,'bs', marker='.', linestyle='solid')


       plt.tight_layout(pad=3)


#Plot2 log(Sigma) vs rank
    def plot2(self):
        SVD_plots.ax[1].set_title('log(Sigma) vs rank')
        SVD_plots.ax[1].set_xlabel('rank')
        SVD_plots.ax[1].set_ylabel('Log(sigma)')
        SVD_plots.ax[1].grid(color = 'grey', linestyle = '--', linewidth = 0.3)
        SVD_plots.ax[1].xaxis.set_ticks(np.arange(min(self.xaxis_points),max(self.xaxis_points)+1 ,1))
        SVD_plots.ax[1].plot(self.xaxis_points,self.S_log,'g')

        plt.tight_layout(pad=3)


#Plot3 Cumulative (S) vs rank. 99% Cut off line attached
    def plot3(self):
        y_range=round((max(self.S_cum)-min(self.S_cum))/500)
        if y_range==0:
            Ystep=50
        else:
           Ystep=y_range*100
        cut_off=0.99* max(self.S_cum)
        SVD_plots.ax[2].set_title('Cumulative(Sigma) vs rank')
        SVD_plots.ax[2].set_xlabel('rank')
        SVD_plots.ax[2].set_ylabel('Cumulative(sigma)')
        SVD_plots.ax[2].grid(color = 'grey', linestyle = '--', linewidth = 0.3)
        SVD_plots.ax[2].yaxis.set_ticks(np.arange(min(self.S_cum),max(self.S_cum)+Ystep ,Ystep))
        SVD_plots.ax[2].xaxis.set_ticks(np.arange(min(self.xaxis_points),max(self.xaxis_points)+1 ,1))
        SVD_plots.ax[2].axhline(y=cut_off, xmin=0, xmax=1 ,color='purple',linestyle = '--',linewidth = 0.7)
        SVD_plots.ax[2].text(max(self.xaxis_points)+0.8,max(self.S_cum),'----- 99% Energy line', color= 'purple')
        SVD_plots.ax[2].plot(self.xaxis_points,self.S_cum,'k')

        plt.tight_layout(pad=3)


#2021-05-12 Anything below here in this script is not used in the program.

#Save as function not used in the program
    def save_as(self):

        save_image=tk.Tk()
        frame7=tk.Frame(save_image)
        frame7.pack()
        save_image.title("Save as")
        save_image.geometry('300x200')

        textbox7=tk.Text(frame7,width=30, height=1, bg='Grey', bd=4)
        textbox7.pack(pady=10)
        textbox7.insert(tk.END,"Do you want to save the image?")

        def save_yes_command():
           SVD_plots.confirm_save=1
           save_image.destroy()

        def save_no_command():
           save_image.destroy()

        save_yes = tk.Button(frame7, text="Yes", bg="green",fg="Black",command=save_yes_command)
        save_yes.pack(side = tk.BOTTOM)
        
        save_no = tk.Button(frame7, text="No", bg="blue",fg="Black",command=save_no_command)
        save_no.pack(side = tk.BOTTOM)

        def shutdown():
          if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            exit()

        save_image.protocol("WM_DELETE_WINDOW", shutdown)

        save_image.mainloop()

    def save_name(self):
        save_name=tk.Tk()
        frame8=tk.Frame(save_name)
        frame8.pack()
        save_name.title("Save as")
        save_name.geometry('300x200')

        save_label=tk.Label(frame8, text="Please select the file format and enter a name ")
        save_label.pack(pady=10)

        entry_save_as=tk.Entry(frame8,width=25)
        entry_save_as.pack(side=tk.TOP)

        formats=tk.StringVar(frame8)
        formats.set(".png")
        cfg_options=tk.OptionMenu(frame8,formats,".png", ".jpg",".pdf")
        cfg_options.pack(pady=10,side = tk.TOP)

        def save_yes_command():
           get_name=entry_save_as.get()
           get_format=formats.get()
           saving_as=get_name + get_format
           SVD_plots.fig.suptitle(saving_as, fontsize=10)
           SVD_plots.fig.savefig(saving_as)
           save_name.destroy()

        save_yes = tk.Button(frame8, text="Confirm", bg="green",fg="Black",command=save_yes_command)
        save_yes.pack(pady=10,side = tk.BOTTOM)

        save_name.mainloop()


    def userplot(self):
        #if id==0:
          self.plot1()
          self.plot2()
          self.plot3()
          plt.show()
          """
        elif id==1:
          self.plot1()
          self.plot2()
          self.plot3()
          self.save_name()



        if SVD_plots.confirm_save==1:
            self.save_name()
        SVD_plots.confirm_save==0

"""

