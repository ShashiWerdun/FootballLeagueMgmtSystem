from tkinter import *

from PIL import ImageTk, Image


class template:

    def __init__(self, master):
        self.master = master
        self.baseFrame = Frame(master)
        self.screenwidth = master.winfo_screenwidth()
        self.screenheight = master.winfo_screenheight()
        self.backimage = ImageTk.PhotoImage(Image.open("Images\\arrow.png").resize((40, 40), Image.ANTIALIAS))
        self.back_button = Button(self.baseFrame, image=self.backimage, font=("Verdana", 16, "bold"), borderwidth=1)


    def start_frame(self):
        self.back_button.place(x=10, y=10)
        self.baseFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def destroy_frame(self):
        self.baseFrame.place_forget()
