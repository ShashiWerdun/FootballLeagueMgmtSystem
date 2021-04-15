from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from ScreenTemplate import template
from tkinter import messagebox


class loginScreenFrame(template):

    def refresh_db(self):
        self.open_a_connection()
        self.acursor.execute("select * from usr")
        self.locallist.clear()
        for user in self.acursor:
            self.locallist.append(user)
        self.close_a_connection()


    def __init__(self, master):
        self.locallist = []
        super().__init__(master)
        self.login_frame = Frame(self.baseFrame)
        img_raw = Image.open('Images\SplashScreen.jpeg')
        img_raw = img_raw.resize((self.screenwidth, self.screenheight), Image.ANTIALIAS)
        img_raw = img_raw.filter(ImageFilter.GaussianBlur(3))
        self.photo = ImageTk.PhotoImage(img_raw)
        self.pic = Label(self.login_frame, image=self.photo)
        self.pic.pack()
        self.frame_login = Frame(self.login_frame, bg="Lemon Chiffon", borderwidth=0)
        self.frame_login.place(x=525, y=300, width=550, height=315)
        Label(self.frame_login, text="Login Screen", font=("Verdana", 16, "bold"), bg="Lemon Chiffon").place(x=200,
                                                                                                             y=20)
        Label(self.frame_login, text="Username", font=("Goudy old style", 13), bg="Lemon Chiffon").place(x=100, y=75)
        self.userentry = Entry(self.frame_login, font=("times new roman", 12))
        self.userentry.place(x=200, y=75)
        Label(self.frame_login, text="Password", font=("Goudy old style", 13), bg="Lemon Chiffon").place(x=100, y=125)
        self.pwdentry = Entry(self.frame_login, font=("times new roman", 12), show='•')
        self.pwdentry.place(x=200, y=125)
        self.loginbutton = Button(self.frame_login, text="LOGIN", font=("Helvetica", 11, "bold"), borderwidth=1,
                                  bg="#990F02", fg="white")
        self.loginbutton.place(x=250, y=175)
        self.anonylogin = Button(self.frame_login, text="Anonymous Login", font=("Helvetica", 11, "bold"), bg="#990F02",
                                 relief="groove", fg="white")
        self.anonylogin.place(x=400, y=230)
        self.registerbutton = Button(self.frame_login, text="New Fan?|Signup Here!", font=("Helvetica", 11, "bold"),
                                     relief="groove", fg="white",
                                     bg="#990F02")
        self.registerbutton.place(x=50, y=230)
        Label(self.frame_login, text="Contact us at: f20190171@hyderabad.bits-pilani.ac.in", font=("Helvetica", 10),
              bg="Lemon Chiffon").place(x=225,
                                        y=280)
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)

    def validate(self):
        self.refresh_db()
        username_entered = self.userentry.get()
        pass_entered = self.pwdentry.get()
        self.userentry.delete(0, 'end')
        self.pwdentry.delete(0, 'end')
        for user in self.locallist:
            if user[0] == username_entered and user[1] == pass_entered:
                return True
        messagebox.showwarning("Login Failed", "Invalid Credentials")
        return False