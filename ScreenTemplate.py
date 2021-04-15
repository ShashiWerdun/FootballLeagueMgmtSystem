from tkinter import *

from PIL import ImageTk, Image
import cx_Oracle

class template:

    def __init__(self, master):
        # BG image
        self.bgimage = ImageTk.PhotoImage(
            Image.open("Images/bgnew.jpg").resize((master.winfo_screenwidth(), master.winfo_screenheight()),
                                                  Image.ANTIALIAS))
        self.dsn_tns = cx_Oracle.makedsn('LAPTOP-V91679QP', '1521', service_name='XE')
        self.master = master
        self.baseFrame = Frame(master)
        self.screenwidth = master.winfo_screenwidth()
        self.screenheight = master.winfo_screenheight()
        self.bg = Label(self.baseFrame, image=self.bgimage).place(x=0, y=0)
        self.backimage = ImageTk.PhotoImage(Image.open("Images\\arrow.png").resize((40, 40), Image.ANTIALIAS))
        self.back_button = Button(self.baseFrame, image=self.backimage, font=("Verdana", 16, "bold"), borderwidth=1)


    def start_frame(self):
        self.back_button.place(x=10, y=10)
        self.baseFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def destroy_frame(self):
        self.baseFrame.place_forget()

    def open_a_connection(self):
        self.forscreenconn = cx_Oracle.connect('dbms_files', 'dbms', dsn=self.dsn_tns)
        self.acursor = self.forscreenconn.cursor()

    def close_a_connection(self):
        self.forscreenconn.commit()
        self.acursor.close()
        self.forscreenconn.close()