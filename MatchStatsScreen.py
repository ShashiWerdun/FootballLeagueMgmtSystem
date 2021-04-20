import tkinter.font as tkFont
from tkinter import *

from PIL import Image, ImageTk

from ScreenTemplate import template


class MatchStatsScreen(template):
    def __init__(self, master, id=None):
        if id is not None:
            super().__init__(master)
            self.MatchStatFrame = Frame(self.baseFrame)
            # required
            font = tkFont.Font(family="Goudy old style", size=18)

            # database connection
            self.open_a_connection()
            self.acursor.execute(f"select * from match where mid = {id}")
            self.match_stats = list(self.acursor.fetchone())
            self.acursor.execute(f"select tname, goals from match_team where mid = {id}")
            self.team_goals = [list(row) for row in self.acursor]
            if self.match_stats[3] is None:
                self.team_goals[0][1] = ''
                self.team_goals[1][1] = ''
                self.total_goals = 'NA'
                self.match_stats[3] = 'NA'
            else:
                self.total_goals = self.team_goals[0][1] + self.team_goals[1][1]

            # display stadium picture

            stadium_pic_raw = Image.open(f'Images\Stadium\{self.match_stats[5].lower()}.jpg')
            stadium_pic_raw = stadium_pic_raw.resize((self.screenwidth // 4, self.screenheight // 4), Image.ANTIALIAS)
            self.stadium_pic = ImageTk.PhotoImage(stadium_pic_raw)
            Label(self.MatchStatFrame, image=self.stadium_pic).grid(rowspan=4, columnspan=2, column=2, row=2)

            # match description
            # Fields:
            Label(self.MatchStatFrame, text="Date and Time: ", font=font, borderwidth=3, relief="ridge").grid(row=1,
                                                                                                              column=0,
                                                                                                              sticky=EW)
            Label(self.MatchStatFrame, text="Winner: ", font=font, borderwidth=3, relief="ridge").grid(row=2, column=0,
                                                                                                       sticky=EW)
            Label(self.MatchStatFrame, text="Hosting Team: ", font=font, borderwidth=3, relief="ridge").grid(row=3,
                                                                                                             column=0,
                                                                                                             sticky=EW)
            Label(self.MatchStatFrame, text="Total Goals in match: ", font=font, borderwidth=3, relief="ridge").grid(
                row=4,
                column=0,
                sticky=EW)
            Label(self.MatchStatFrame, text="Stadium Details: ", font=font, borderwidth=3, relief="ridge").grid(row=5,
                                                                                                                column=0,
                                                                                                                sticky=EW)
            # Data:
            datetime_string = str(self.match_stats[1].date()) + ' ' + self.match_stats[2]
            stadium_details = self.match_stats[5] + ', ' + self.match_stats[6]
            Label(self.MatchStatFrame, text=datetime_string, font=font, borderwidth=3, relief="ridge").grid(row=1,
                                                                                                            column=1,
                                                                                                            sticky=EW)
            Label(self.MatchStatFrame, text=self.match_stats[3], font=font, borderwidth=3, relief="ridge").grid(row=2,
                                                                                                                column=1,
                                                                                                                sticky=EW)
            Label(self.MatchStatFrame, text=self.match_stats[4], font=font, borderwidth=3, relief="ridge").grid(row=3,
                                                                                                                column=1,
                                                                                                                sticky=EW)
            Label(self.MatchStatFrame, text=self.total_goals, font=font, borderwidth=3, relief="ridge").grid(row=4,
                                                                                                             column=1,
                                                                                                             sticky=EW)
            Label(self.MatchStatFrame, text=stadium_details, font=font, borderwidth=3,
                  relief="ridge").grid(row=5, column=1, sticky=EW)

            # team performance row
            # teamA image
            teamA_pic_raw = Image.open(f'Images\{self.team_goals[0][0].lower()}.jpg')
            teamA_pic_raw = teamA_pic_raw.resize((self.screenwidth // 10, self.screenheight // 8), Image.ANTIALIAS)
            self.teamA_pic = ImageTk.PhotoImage(teamA_pic_raw)
            Label(self.MatchStatFrame, image=self.teamA_pic).grid(row=0, column=0)
            # text perfomance
            goalsA = self.team_goals[0][1]
            goalsB = self.team_goals[1][1]
            teamA = self.team_goals[0][0]
            teamB = self.team_goals[1][0]
            performance_string = teamA + " " + str(goalsA) + " " + "-" + " " + str(goalsB) + " " + teamB
            Label(self.MatchStatFrame, text=performance_string, font=("Goudy old style", 26, "bold"), borderwidth=4,
                  relief="ridge").grid(row=0, columnspan=2, column=1, sticky=EW)
            # teamB image
            teamB_pic_raw = Image.open(f'Images\{self.team_goals[1][0].lower()}.jpg')
            teamB_pic_raw = teamB_pic_raw.resize((self.screenwidth // 10, self.screenheight // 8), Image.ANTIALIAS)
            self.teamB_pic = ImageTk.PhotoImage(teamB_pic_raw)
            Label(self.MatchStatFrame, image=self.teamB_pic).grid(row=0, column=3)
            # screen frame place
            self.MatchStatFrame.place(x=250, y=300)
