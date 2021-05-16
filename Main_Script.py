from tkinter import *
from tkinter.messagebox import showinfo
import os


class App():
    def __init__(self,master):

        frame=Frame(master)
        frame.pack()

        #Call the current directory (path)
        self.directory=os.getcwd()

        # configure the root window
        master.title("")
        master.geometry('500x333')
        master.iconbitmap(self.directory+'/icon.ico')

        #Background image
        self.f=PhotoImage(file=self.directory+"/background2.png")
        self.label1=Label(master, image=self.f)
        self.label1.pack()

        def button1_cmd():
           master.destroy()
           import Script6
        #Button
        self.button1=Button(master, text="Start" , bg="light grey",fg="Black",command=button1_cmd, width=10, height=2)
        self.button1.place(x=200, y=260)



root=Tk()
A=App(root)
root.mainloop()


