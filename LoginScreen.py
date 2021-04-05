from tkinter import *
from PIL import ImageTk, Image, ImageFilter


class loginScreenFrame:

    def __init__(self, master):
        self.login_frame = Frame(master)
        img_raw = Image.open('Images\SplashScreen.jpeg')
        img_raw = img_raw.resize((master.winfo_screenwidth(), master.winfo_screenheight()), Image.ANTIALIAS)
        img_raw = img_raw.filter(ImageFilter.GaussianBlur(3))
        self.photo = ImageTk.PhotoImage(img_raw)
        self.pic = Label(self.login_frame, image=self.photo)
        self.pic.pack()
        self.frame_login = Frame(self.login_frame, bg="White")
        self.frame_login.place(x=525, y=300, width=550, height=300)
        title = Label(self.frame_login, text="Login Screen", font=("Verdana", 16, "bold")).place(x=200, y=20)
        user_lbl = Label(self.frame_login, text="UserName", font=("Goudy old style", 13)).place(x=70, y=75)
        self.txt_usr = Entry(self.frame_login, font=("times new roman", 12)).place(x=170, y=75)
        pwd_lbl = Label(self.frame_login, text="Password", font=("Goudy old style", 13)).place(x=70, y=125)
        self.txt_pwd = Entry(self.frame_login, font=("times new roman", 12)).place(x=170, y=125)
        login = Button(self.frame_login, text="Login", font=("Goudy old style", 13)).place(x=220, y=175)
        ano_login = Button(self.frame_login, text="Anonymous Login", font=("Goudy old style", 9)).place(x=400, y=230)
        nwfan_login = Button(self.frame_login, text="New Fan?|Signup Here!", font=("Goudy old style", 9)).place(x=50, y=230)
        pwd_lbl = Label(self.frame_login, text="Contact us at:***********", font=("times new roman", 8)).place(x=375, y=275)
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)


