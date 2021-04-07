import datetime
import tkinter.font as tkFont
from tkinter import *

from PIL import ImageTk, Image

from ScreenTemplate import template


class ProfileScreen(template):
    def __init__(self, master):
        super().__init__(master)
        self.profile_frame = Frame(self.baseFrame)

        # display profile picture
        self.dp_raw = Image.open('Images\SplashScreen.jpeg')
        self.dp_raw = self.dp_raw.resize((self.screenwidth // 4, self.screenheight // 4), Image.ANTIALIAS)
        self.dp = ImageTk.PhotoImage(self.dp_raw)
        Label(self.profile_frame, image=self.dp).grid(row=0, columnspan=2)

        # display user's details
        font = tkFont.Font(family="Goudy old style", size=18)
        # create fields
        self.name_field = Label(self.profile_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
            row=1, column=0, sticky=EW)
        self.phoneNumber_field = Label(self.profile_frame, text="Phone Number: ", font=font, borderwidth=3,
                                       relief="ridge").grid(row=2, column=0, sticky=EW)
        self.gender_field = Label(self.profile_frame, text="Gender: ", font=font, borderwidth=3, relief="ridge").grid(
            row=3, column=0, sticky=EW)
        self.dob_field = Label(self.profile_frame, text="Date of birth: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=4, column=0, sticky=EW)
        self.mail_field = Label(self.profile_frame, text="Mail ID: ", font=font, borderwidth=3, relief="ridge").grid(
            row=5, column=0, sticky=EW)
        # fill the details
        self.name = Label(self.profile_frame, text="Shashivardhan", font=font, borderwidth=3, relief="ridge").grid(
            row=1, column=1, sticky=EW)
        self.phoneNumber = Label(self.profile_frame, text="7680973625", font=font, borderwidth=3, relief="ridge").grid(
            row=2, column=1, sticky=EW)
        self.gender = Label(self.profile_frame, text="male", font=font, borderwidth=3, relief="ridge").grid(row=3,
                                                                                                            column=1,
                                                                                                            sticky=EW)
        date_string = datetime.date(year=2002, day=20, month=1)
        self.dob = Label(self.profile_frame, text=date_string, font=font, borderwidth=3, relief="ridge").grid(row=4,
                                                                                                              column=1,
                                                                                                              sticky=EW)
        self.mail = Label(self.profile_frame, text="shashivardhan201@gmail.com", font=font, borderwidth=3,
                          relief="ridge").grid(row=5, column=1, sticky=EW)

        # display the final frame
        pos_x = 3 * self.screenwidth // 8 - 75
        pos_y = self.screenheight // 4
        # self.profile_frame.grid(sticky="")
        self.profile_frame.place(x=pos_x, y=pos_y)
