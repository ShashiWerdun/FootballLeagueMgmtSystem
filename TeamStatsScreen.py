import tkinter.font as tkFont
from tkinter import *

from PIL import ImageTk, Image

from ScreenTemplate import template


class TeamStatsScreen(template):
    def __init__(self, master):
        super().__init__(master)
        self.teamStat_frame = Frame(self.baseFrame)

        # display player picture
        dp_raw = Image.open('Images\SplashScreen.jpeg')
        dp_raw = dp_raw.resize((self.screenwidth // 4, self.screenheight // 4), Image.ANTIALIAS)
        self.dp = ImageTk.PhotoImage(dp_raw)
        pic = Label(self.teamStat_frame, image=self.dp)
        pic.grid(column=0, rowspan=4)

        # display player's details
        font = tkFont.Font(family="Goudy old style", size=18)

        # create fields
        self.name_field = Label(self.teamStat_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
            row=0, column=1, sticky=EW)
        self.ceo_field = Label(self.teamStat_frame, text="CEO: ", font=font, borderwidth=3,
                               relief="ridge").grid(row=1, column=1, sticky=EW)
        self.homestadium_field = Label(self.teamStat_frame, text="Home Stadium: ", font=font, borderwidth=3,
                                       relief="ridge").grid(
            row=2, column=1, sticky=EW)
        self.numcoaches_field = Label(self.teamStat_frame, text="Number of coaches: ", font=font, borderwidth=3,
                                      relief="ridge").grid(row=5, columnspan=2, column=0, sticky=EW)
        self.yrofest_field = Label(self.teamStat_frame, text="Year of establishment: ", font=font, borderwidth=3,
                                   relief="ridge").grid(row=6, columnspan=2, column=0, sticky=EW)
        self.points_field = Label(self.teamStat_frame, text="League points: ", font=font, borderwidth=3,
                                  relief="ridge").grid(row=7, columnspan=2, column=0, sticky=EW)

        # fill the details
        self.name = Label(self.teamStat_frame, text="DBMS Project", font=font, borderwidth=3, relief="ridge").grid(
            row=0, column=2, sticky=EW)
        self.ceo = Label(self.teamStat_frame, text="Chakka", font=font, borderwidth=3, relief="ridge").grid(
            row=1, column=2, sticky=EW)
        self.homestadium = Label(self.teamStat_frame, text="rajiv gandhi airport", font=font, borderwidth=3,
                                 relief="ridge").grid(row=2,
                                                      column=2,
                                                      sticky=EW)
        self.numcoaches = Label(self.teamStat_frame, text="inf", font=font, borderwidth=3, relief="ridge").grid(row=5,
                                                                                                                column=2,
                                                                                                                sticky=EW)
        self.yrofest = Label(self.teamStat_frame, text="2020", font=font, borderwidth=3, relief="ridge").grid(
            row=6,
            column=2,
            sticky=EW)
        self.points = Label(self.teamStat_frame, text="20", font=font, borderwidth=3, relief="ridge").grid(row=7,
                                                                                                           column=2,
                                                                                                           sticky=EW)

        # display the final frame
        pos_x = 3 * self.screenwidth // 8 - 200
        pos_y = self.screenheight // 4
        # self.profile_frame.grid(sticky="")
        self.teamStat_frame.place(x=pos_x, y=pos_y)
