import tkinter.font as tkFont
from tkinter import *

from PIL import ImageTk, Image

from ScreenTemplate import template


class PlayerStatsScreen(template):

    def __init__(self, master, id=None):
        if id is not None:
            super().__init__(master)
            self.playerStat_frame = Frame(self.baseFrame)
            self.pname = id[0]

            # data retrival
            self.open_a_connection()
            self.acursor.execute(
                f"select name, rank, DOB, nation, team, MPPOS from participant natural join player where name='{self.pname}'")
            self.player = list(self.acursor)
            self.close_a_connection()
            self.player = list(self.player[0])
            # display player picture
            dp_raw = Image.open(f'Images\{self.player[0].lower()}.jpg')
            dp_raw = dp_raw.resize((400, 400), Image.ANTIALIAS)
            self.dp = ImageTk.PhotoImage(dp_raw)
            pic = Label(self.baseFrame, image=self.dp)
            pic.place(x=265, y=230)
            # display player's details
            font = tkFont.Font(family="@HP Simplified Jpan", size=28)

            # create fields
            Label(self.playerStat_frame, text="Name: ", font=font, borderwidth=3, relief="ridge").grid(
                row=0, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text="Rank: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=1, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text="Born on: ", font=font, borderwidth=3,
                  relief="ridge").grid(
                row=2, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text="Nationality: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=3, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text="Belongs to: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=4, column=0, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text="Most played position: ", font=font, borderwidth=3,
                  relief="ridge").grid(row=5, column=0, sticky=EW, ipadx=10, ipady=5)

            # fill the details
            Label(self.playerStat_frame, text=self.player[0], font=font, borderwidth=3, relief="ridge").grid(
                row=0, column=1, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text=self.player[1], font=font, borderwidth=3, relief="ridge").grid(
                row=1, column=1, sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text=self.player[2].date(), font=font, borderwidth=3,
                  relief="ridge").grid(row=2,
                                       column=1,
                                       sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text=self.player[3], font=font, borderwidth=3,
                  relief="ridge").grid(row=3,
                                       column=1,
                                       sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text=self.player[4], font=font, borderwidth=3,
                  relief="ridge").grid(
                row=4,
                column=1,
                sticky=EW, ipadx=10, ipady=5)
            Label(self.playerStat_frame, text=self.player[5], font=font, borderwidth=3, relief="ridge").grid(
                row=5,
                column=1,
                sticky=EW, ipadx=10, ipady=5)

            # display the final frame
            self.playerStat_frame.place(x=700, y=225)
