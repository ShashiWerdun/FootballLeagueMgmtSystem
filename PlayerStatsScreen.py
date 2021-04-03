from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import datetime


class PlayerStatsScreen:
    def __init__(self, master):
        self.playerStat_frame = Frame(master)
        # required
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # display player picture
        dp_raw = Image.open('Images\SplashScreen.jpeg')
        dp_raw = dp_raw.resize((screen_width // 4, screen_height // 4), Image.ANTIALIAS)
        self.dp = ImageTk.PhotoImage(dp_raw)
        pic = Label(self.playerStat_frame, image=self.dp)
        pic.grid(column=0, rowspan=4)

        # display player's details
        font = tkFont.Font(family="Goudy old style", size=18)

        # create fields
        self.name_field = Label(self.playerStat_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
            row=0, column=1, sticky=EW)
        self.age_field = Label(self.playerStat_frame, text="Age: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=1, column=1, sticky=EW)
        self.gender_field = Label(self.playerStat_frame, text="Gender: ", font=font, borderwidth=3,
                                  relief="ridge").grid(
            row=2, column=1, sticky=EW)
        self.dob_field = Label(self.playerStat_frame, text="Date of birth: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=3, column=1, sticky=EW)
        self.nation_field = Label(self.playerStat_frame, text="Nationality: ", font=font, borderwidth=3,
                                  relief="ridge").grid(row=4, column=1, sticky=EW)
        self.sal_field = Label(self.playerStat_frame, text="Base salary: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=5, columnspan=2, column=0, sticky=EW)
        self.mppos_field = Label(self.playerStat_frame, text="Most played position: ", font=font, borderwidth=3,
                                 relief="ridge").grid(row=6, columnspan=2, column=0, sticky=EW)
        self.goals_field = Label(self.playerStat_frame, text="League goals: ", font=font, borderwidth=3,
                                 relief="ridge").grid(row=7, columnspan=2, column=0, sticky=EW)
        self.rank_field = Label(self.playerStat_frame, text="League Rank: ", font=font, borderwidth=3,
                                relief="ridge").grid(row=8, columnspan=2, column=0, sticky=EW)

        # fill the details
        self.name = Label(self.playerStat_frame, text="Shashivardhan", font=font, borderwidth=3, relief="ridge").grid(
            row=0, column=2, sticky=EW)
        self.age = Label(self.playerStat_frame, text="19", font=font, borderwidth=3, relief="ridge").grid(
            row=1, column=2, sticky=EW)
        self.gender = Label(self.playerStat_frame, text="male", font=font, borderwidth=3, relief="ridge").grid(row=2,
                                                                                                               column=2,
                                                                                                               sticky=EW)
        date_string = datetime.date(year=2002, day=20, month=1)
        self.dob = Label(self.playerStat_frame, text=date_string, font=font, borderwidth=3, relief="ridge").grid(row=3,
                                                                                                                 column=2,
                                                                                                                 sticky=EW)
        self.nation = Label(self.playerStat_frame, text="Indian", font=font, borderwidth=3,
                            relief="ridge").grid(row=4, column=2, sticky=EW)
        self.sal = Label(self.playerStat_frame, text="10,000K", font=font, borderwidth=3, relief="ridge").grid(row=5,
                                                                                                               column=2,
                                                                                                               sticky=EW)
        self.mppos = Label(self.playerStat_frame, text="Left Forward", font=font, borderwidth=3, relief="ridge").grid(
            row=6,
            column=2,
            sticky=EW)
        self.goals = Label(self.playerStat_frame, text="20", font=font, borderwidth=3, relief="ridge").grid(row=7,
                                                                                                            column=2,
                                                                                                            sticky=EW)
        self.rank = Label(self.playerStat_frame, text="#5", font=font, borderwidth=3, relief="ridge").grid(row=8,
                                                                                                           column=2,
                                                                                                           sticky=EW)

        # display the final frame
        pos_x = 3 * screen_width // 8 - 200
        pos_y = screen_height // 4
        # self.profile_frame.grid(sticky="")
        self.playerStat_frame.place(x=pos_x, y=pos_y)
