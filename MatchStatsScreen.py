import datetime
import tkinter.font as tkFont
from tkinter import *

from PIL import Image, ImageTk


class MatchStatsScreen:
    def __init__(self, master):
        self.MatchStatFrame = Frame(master)
        # required
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        font = tkFont.Font(family="Goudy old style", size=18)

        # display stadium picture
        stadium_pic_raw = Image.open('Images\SplashScreen.jpeg')
        stadium_pic_raw = stadium_pic_raw.resize((screen_width // 4, screen_height // 4), Image.ANTIALIAS)
        self.stadium_pic = ImageTk.PhotoImage(stadium_pic_raw)
        Label(self.MatchStatFrame, image=self.stadium_pic).grid(rowspan=4, columnspan=2, column=2)

        # match description
        # Fields:
        Label(self.MatchStatFrame, text="Date and Time: ", font=font, borderwidth=3, relief="ridge").grid(row=0,
                                                                                                          column=0,
                                                                                                          sticky=EW)
        Label(self.MatchStatFrame, text="Winner: ", font=font, borderwidth=3, relief="ridge").grid(row=1, column=0,
                                                                                                   sticky=EW)
        Label(self.MatchStatFrame, text="Hosting Team: ", font=font, borderwidth=3, relief="ridge").grid(row=2,
                                                                                                         column=0,
                                                                                                         sticky=EW)
        Label(self.MatchStatFrame, text="Total Goals in match: ", font=font, borderwidth=3, relief="ridge").grid(row=3,
                                                                                                                 column=0,
                                                                                                                 sticky=EW)
        Label(self.MatchStatFrame, text="Stadium Details: ", font=font, borderwidth=3, relief="ridge").grid(row=4,
                                                                                                            column=0,
                                                                                                            sticky=EW)
        # Data:
        datetime_string = datetime.datetime(year=2021, month=4, day=9, hour=16, minute=30)
        Label(self.MatchStatFrame, text=datetime_string, font=font, borderwidth=3, relief="ridge").grid(row=0, column=1,
                                                                                                        sticky=EW)
        Label(self.MatchStatFrame, text="Pakistan", font=font, borderwidth=3, relief="ridge").grid(row=1, column=1,
                                                                                                   sticky=EW)
        Label(self.MatchStatFrame, text="Pakistan", font=font, borderwidth=3, relief="ridge").grid(row=2, column=1,
                                                                                                   sticky=EW)
        Label(self.MatchStatFrame, text="inf", font=font, borderwidth=3, relief="ridge").grid(row=3, column=1,
                                                                                              sticky=EW)
        Label(self.MatchStatFrame, text="Pakistani international stadium, pakistan", font=font, borderwidth=3,
              relief="ridge").grid(row=4, column=1, sticky=EW)

        # team performance
        goalsA = 3
        goalsB = 1
        teamA = "Pakistan"
        teamB = "No-one"
        performance_string = teamA + " " + str(goalsA) + " " + "-" + " " + str(goalsB) + " " + teamB
        self.performance_frame = Frame(self.MatchStatFrame).grid(row=5, columnspan=4, sticky=EW)
        Label(self.MatchStatFrame, text=performance_string, font=("Goudy old style", 26, "bold"), borderwidth=4,
              relief="ridge").grid(
            row=5, columnspan=4, sticky=EW)

    def start_frame(self):
        self.MatchStatFrame.place(x=250, y=200)
