from tkinter import *

class loginScreenFrame:

    def __init__(self, master, image):
        self.loginframe = Frame(master)
        width = master.winfo_screenwidth()
        height = master.winfo_screenheight()
        Label(self.loginframe, text="Username:").place(x=250, y=250)
        #Entry(self.loginframe).place(relx=0.6,rely=0.5)
        #Label(self.loginframe, text="Password:").place(relx=0.5, rely=0.6)
        #Entry(self.loginframe).place(relx=0.6, rely=0.6)
        self.loginframe.place(x=0,y=0,height=400, width=400)