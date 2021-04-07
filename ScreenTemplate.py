from tkinter import *


class template:

    def __init__(self, master):
        self.master = master
        self.baseFrame = Frame(master)
        self.screenwidth = master.winfo_screenwidth()
        self.screenheight = master.winfo_screenheight()

        '''self.back_button = Button(self.baseFrame, text="BACK", font=("Verdana", 16, "bold"), borderwidth=3,
                                  relief="ridge")
        self.back_button.place(x=0, y=0)'''

    def start_frame(self):
        self.baseFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def destroy_frame(self):
        self.baseFrame.place_forget()
