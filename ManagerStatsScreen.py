from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import datetime


class ManagerStatsScreen:
    def __init__(self, master):
        self.managerStat_frame = Frame(master)
        # required
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # display player picture
        dp_raw = Image.open('Images\SplashScreen.jpeg')
        dp_raw = dp_raw.resize((screen_width // 4, screen_height // 4), Image.ANTIALIAS)
        self.dp = ImageTk.PhotoImage(dp_raw)
        pic = Label(self.managerStat_frame, image=self.dp)
        pic.grid(column=0, rowspan=4)

        # display player's details
        font = tkFont.Font(family="Goudy old style", size=18)

        # create fields
        self.name_field = Label(self.managerStat_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
            row=0, column=1, sticky=EW)
        self.age_field = Label(self.managerStat_frame, text="Age: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=1, column=1, sticky=EW)
        self.gender_field = Label(self.managerStat_frame, text="Gender: ", font=font, borderwidth=3,
                                  relief="ridge").grid(
            row=2, column=1, sticky=EW)
        self.dob_field = Label(self.managerStat_frame, text="Date of birth: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=3, column=1, sticky=EW)
        self.nation_field = Label(self.managerStat_frame, text="Nationality: ", font=font, borderwidth=3,
                                  relief="ridge").grid(row=4, column=1, sticky=EW)
        self.hiredate_field = Label(self.managerStat_frame, text="Hire Date: ", font=font, borderwidth=3,
                                    relief="ridge").grid(row=5, columnspan=2, column=0, sticky=EW)
        self.joindate_field = Label(self.managerStat_frame, text="Join Date: ", font=font, borderwidth=3,
                                    relief="ridge").grid(row=6, columnspan=2, column=0, sticky=EW)
        self.exp_field = Label(self.managerStat_frame, text="Experience: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=7, columnspan=2, column=0, sticky=EW)

        # fill the details
        self.name = Label(self.managerStat_frame, text="Shashivardhan", font=font, borderwidth=3, relief="ridge").grid(
            row=0, column=2, sticky=EW)
        self.age = Label(self.managerStat_frame, text="19", font=font, borderwidth=3, relief="ridge").grid(
            row=1, column=2, sticky=EW)
        self.gender = Label(self.managerStat_frame, text="male", font=font, borderwidth=3, relief="ridge").grid(row=2,
                                                                                                                column=2,
                                                                                                                sticky=EW)
        dob_string = datetime.date(year=2002, day=20, month=1)
        self.dob = Label(self.managerStat_frame, text=dob_string, font=font, borderwidth=3, relief="ridge").grid(row=3,
                                                                                                                 column=2,
                                                                                                                 sticky=EW)
        self.nation = Label(self.managerStat_frame, text="Indian", font=font, borderwidth=3,
                            relief="ridge").grid(row=4, column=2, sticky=EW)
        hiredate_string = datetime.date(year=2019, day=1, month=8)
        self.hiredate = Label(self.managerStat_frame, text=hiredate_string, font=font, borderwidth=3,
                              relief="ridge").grid(row=5,
                                                   column=2,
                                                   sticky=EW)
        joindate_string = datetime.date(year=2019, day=1, month=8)
        self.joindate = Label(self.managerStat_frame, text=joindate_string, font=font, borderwidth=3,
                              relief="ridge").grid(
            row=6,
            column=2,
            sticky=EW)
        self.exp = Label(self.managerStat_frame, text="20Y", font=font, borderwidth=3, relief="ridge").grid(row=7,
                                                                                                            column=2,
                                                                                                            sticky=EW)

        # display the final frame
        pos_x = 3 * screen_width // 8 - 200
        pos_y = screen_height // 4
        # self.profile_frame.grid(sticky="")
        self.managerStat_frame.place(x=pos_x, y=pos_y)
