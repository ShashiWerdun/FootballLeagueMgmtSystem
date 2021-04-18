import tkinter.font as tkFont
from tkinter import *

from PIL import ImageTk, Image

from ScreenTemplate import template


class TeamStatsScreen(template):

    def __init__(self, master, id=None):
        if id is not None:
            super().__init__(master)
            self.teamStat_frame = Frame(self.baseFrame)
            self.tname = id[0]

            # data retrival
            self.open_a_connection()
            self.acursor.execute(f"select * from team where tname='{self.tname}'")
            self.team = list(self.acursor)
            self.close_a_connection()
            self.team = list(self.team[0])
            # display player picture
            dp_raw = Image.open(f'Images\{self.team[1].lower()}.jpeg')
            dp_raw = dp_raw.resize((400, 400), Image.ANTIALIAS)
            self.dp = ImageTk.PhotoImage(dp_raw)
            pic = Label(self.baseFrame, image=self.dp)
            pic.place(x=265, y=230)
            # display player's details
            font = tkFont.Font(family="@HP Simplified Jpan", size=30)

            # create fields
            Label(self.teamStat_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
                row=0, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text="CEO: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=1, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text="Home Stadium: ", font=font, borderwidth=3,
                  relief="ridge").grid(
                row=2, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text="Number of coaches: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=3, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text="Year of establishment: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=4, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text="League points: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=5, column=0, sticky=EW, ipadx=10, ipady=5)

            # fill the details
            Label(self.teamStat_frame, text=self.team[1], font=font, borderwidth=3, relief="ridge").grid(
                row=0, column=1, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text=self.team[2], font=font, borderwidth=3, relief="ridge").grid(
                row=1, column=1, sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text=self.team[-1], font=font, borderwidth=3,
                  relief="ridge").grid(row=2,
                                       column=1,
                                       sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text=self.team[0], font=font, borderwidth=3,
                  relief="ridge").grid(row=3,
                                       column=1,
                                       sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text=self.team[-2], font=font, borderwidth=3,
                  relief="ridge").grid(
                row=4,
                column=1,
                sticky=EW, ipadx=10, ipady=5)
            Label(self.teamStat_frame, text=self.team[-3], font=font, borderwidth=3, relief="ridge").grid(
                row=5,
                column=1,
                sticky=EW, ipadx=10, ipady=5)

            # display the final frame
            self.teamStat_frame.place(x=700, y=225)
