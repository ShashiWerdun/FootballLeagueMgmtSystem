from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from HomePage import HomeScreenFrameGen
from reg_screen import Reg_screen
from ScreenTemplate import template

class loginScreenFrame(template):

    def __init__(self, master):
        self.master = master
        self.login_frame = Frame(master)
        super().__init__(self.login_frame)
        img_raw = Image.open('Images\SplashScreen.jpeg')
        img_raw = img_raw.resize((master.winfo_screenwidth(), master.winfo_screenheight()), Image.ANTIALIAS)
        img_raw = img_raw.filter(ImageFilter.GaussianBlur(3))
        self.photo = ImageTk.PhotoImage(img_raw)
        self.pic = Label(self.login_frame, image=self.photo)
        self.pic.pack()
        self.frame_login = Frame(self.login_frame, bg="White", relief=RAISED, borderwidth=0)
        self.frame_login.place(x=525, y=300, width=550, height=315)
        Label(self.frame_login, text="Login Screen", font=("Verdana", 16, "bold"), bg="White").place(x=200, y=20)
        Label(self.frame_login, text="Username", font=("Goudy old style", 13),bg="White").place(x=100, y=75)
        self.userentry = Entry(self.frame_login, font=("times new roman", 12),bg="White")
        self.userentry.place(x=200, y=75)
        Label(self.frame_login, text="Password", font=("Goudy old style", 13),bg="White").place(x=100, y=125)
        self.pwdentry = Entry(self.frame_login, font=("times new roman", 12),bg="White")
        self.pwdentry.place(x=200, y=125)
        self.loginbutton = Button(self.frame_login, text="Login", font=("Goudy old style", 13), borderwidth=1)
        self.loginbutton.place(x=220, y=175)
        self.anonylogin = Button(self.frame_login, text="Anonymous Login", font=("Goudy old style", 9),bg="White")
        self.anonylogin.place(x=400, y=230)
        self.registerbutton = Button(self.frame_login, text="New Fan?|Signup Here!", font=("Goudy old style", 9),bg="White")
        self.registerbutton.place(x=50, y=230)
        Label(self.frame_login, text="Contact us at:***********", font=("times new roman", 8),bg="White").place(x=375, y=275)

    def start_frame(self):
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)
