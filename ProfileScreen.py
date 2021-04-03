from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import tkinter.font as tkFont
from tkcalendar import Calendar, DateEntry
import datetime


class ProfileScreen:
    def __init__(self, master):
        self.profile_frame = Frame(master)
        # required
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # display profile picture
        dp_raw = Image.open('Images\SplashScreen.jpeg')
        dp_raw = dp_raw.resize((screen_width // 4, screen_height // 4), Image.ANTIALIAS)
        self.dp = ImageTk.PhotoImage(dp_raw)
        pic = Label(self.profile_frame, image=self.dp)
        pic.grid(row=0, columnspan=2)

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
        pos_x = 3 * screen_width // 8 - 75
        pos_y = screen_height // 4
        # self.profile_frame.grid(sticky="")
        self.profile_frame.place(x=pos_x, y=pos_y)
