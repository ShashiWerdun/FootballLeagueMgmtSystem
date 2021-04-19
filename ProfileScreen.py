import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from ScreenTemplate import template


class ProfileScreen(template):
    def __init__(self, master, uid=None):
        if uid is not None:
            super().__init__(master)
            self.profile_frame = Frame(self.baseFrame)
            # general font for this page
            font = tkFont.Font(family="Goudy old style", size=18)

            # database connection
            self.open_a_connection()
            self.acursor.execute(f"select name, phnum, gender, dob, mail from fan where fid = {uid}")
            self.user_details = list(self.acursor.fetchone())

            # Favourites button
            self.style = ttk.Style()
            self.style.theme_use("clam")
            self.style.configure("profile.TButton", font=("Malgun Gothic", 12, "bold"))
            self.favourites_image = ImageTk.PhotoImage(Image.open("Images/lover.png"))
            self.favourites_button = ttk.Button(self.baseFrame, image=self.favourites_image, compound=TOP,
                                                text="Favourites", style="profile.TButton")
            self.favourites_button.place(x=950, y=150)

            # create fields
            self.profile_frame.columnconfigure(0, minsize=200)
            self.name_field = Label(self.profile_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
                row=1, column=0, sticky=EW)
            self.phoneNumber_field = Label(self.profile_frame, text="Phone Number: ", font=font, borderwidth=3,
                                           relief="ridge").grid(row=2, column=0, sticky=EW)
            self.gender_field = Label(self.profile_frame, text="Gender: ", font=font, borderwidth=3,
                                      relief="ridge").grid(
                row=3, column=0, sticky=EW)
            self.dob_field = Label(self.profile_frame, text="Date of birth: ", font=font, borderwidth=3,
                                   relief="ridge").grid(row=4, column=0, sticky=EW)
            self.mail_field = Label(self.profile_frame, text="Mail ID: ", font=font, borderwidth=3,
                                    relief="ridge").grid(
                row=5, column=0, sticky=EW)

            # fill the details
            self.profile_frame.columnconfigure(1, minsize=400)
            self.name = Label(self.profile_frame, text=self.user_details[0], font=font, borderwidth=3,
                              relief="ridge").grid(
                row=1, column=1, sticky=EW)
            self.phoneNumber = Label(self.profile_frame, text=self.user_details[1], font=font, borderwidth=3,
                                     relief="ridge").grid(
                row=2, column=1, sticky=EW)
            self.gender = Label(self.profile_frame, text=self.user_details[2], font=font, borderwidth=3,
                                relief="ridge").grid(row=3,
                                                     column=1,
                                                     sticky=EW)
            self.dob = Label(self.profile_frame, text=self.user_details[3].strftime("%d-%m-%Y"), font=font,
                             borderwidth=3, relief="ridge").grid(row=4,
                                                                 column=1,
                                                                 sticky=EW)
            self.mail = Label(self.profile_frame, text=self.user_details[4], font=font, borderwidth=3,
                              relief="ridge").grid(row=5, column=1, sticky=EW)

            # display profile picture
            self.dp_raw = Image.open('Images\SplashScreen.jpeg')
            self.dp_raw = self.dp_raw.resize((250, 250), Image.ANTIALIAS)
            self.dp = ImageTk.PhotoImage(self.dp_raw)
            Label(self.baseFrame, image=self.dp).place(x=650, y=200)

            # display the final frame
            pos_x = 3 * self.screenwidth // 8 - 100
            pos_y = self.screenheight // 2 + 50
            self.profile_frame.place(x=pos_x, y=pos_y)
