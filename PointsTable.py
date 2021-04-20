from tkinter import *
from tkinter import ttk

from ScreenTemplate import template


class pointsTableFrame(template):

    def __init__(self, master):
        super().__init__(master)
        self.tree_frame = Frame(self.baseFrame)
        self.tree_frame.pack(pady=150)
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        self.usable_frame = Frame(self.tree_frame)

        # get data from database
        self.open_a_connection()
        self.acursor.execute("select tname, pts from team order by pts desc")
        self.teams_list = [team for team in self.acursor.fetchall()]
        print(self.teams_list)
        self.rows = []
        for team in self.teams_list:
            team_row = []
            points = team[1]
            team = team[0]
            team_row.append(team)
            self.acursor.execute(f"select count(*) from match_team where tname = '{team}'")
            played = (self.acursor.fetchone())[0]
            team_row.append(played)
            self.acursor.execute(f"select count(*) from match where winner='{team}'")
            wins = (self.acursor.fetchone())[0]
            team_row.append(wins)
            self.acursor.execute(
                f"select count(*) from match m, match_team mt where winner is NULL and m.mid = mt.mid and mt.tname='{team}'")
            draws = (self.acursor.fetchone())[0]
            team_row.append(draws)
            self.acursor.execute(
                f"select count(*) from match where winner!='{team}' and winner is not NULL and mid in (select mid from match_team where tname='{team}')")
            losses = (self.acursor.fetchone())[0]
            team_row.append(losses)
            self.acursor.execute(f"select sum(goals) from match_team where tname='{team}'")
            goals_for = (self.acursor.fetchone())[0]
            if goals_for is None:
                goals_for = 0
            team_row.append(goals_for)
            self.acursor.execute(
                f"select sum(goals) from match_team where tname!='{team}' and mid in (select mid from match_team where tname='{team}')")
            goals_against = (self.acursor.fetchone())[0]
            if goals_against is None:
                goals_against = 0
            team_row.append(goals_against)
            team_row.append(goals_for - goals_against)
            team_row.append(points)

            print(team_row)
            self.rows.append(team_row)
        print(self.rows)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("pointstable.Treeview", background="Lemon Chiffon", foreground="black", rowheight=50,
                             fieldbackground="cornsilk3")
        self.style.map('pointstable.Treeview', background=[('selected', 'coral4')])
        self.style.configure("pointstable.Treeview.Heading", font=("Malgun Gothic", 12, "bold"))
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, style="pointstable.Treeview")
        self.tree_scroll.config(command=self.my_tree.yview)

        self.my_tree.pack()

        self.my_tree['columns'] = (
            "Position", "Team", "Played", "Wins", "Draws", "Loss", "GF (Goals For)", "GA (Goals Against)",
            "GD (Goals Diff)", "Points")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Position", width=100)
        self.my_tree.column("Team", width=250)
        self.my_tree.column("Played", width=70)
        self.my_tree.column("Wins", width=70)
        self.my_tree.column("Draws", width=70)
        self.my_tree.column("Loss", width=70)
        self.my_tree.column("GF (Goals For)", width=140)
        self.my_tree.column("GA (Goals Against)", width=180)
        self.my_tree.column("GD (Goals Diff)", width=140)
        self.my_tree.column("Points", width=70)

        self.my_tree.heading("#0", text="")
        self.my_tree.heading("Position", text="Position")
        self.my_tree.heading("Team", text="Team")
        self.my_tree.heading("Played", text="Played")
        self.my_tree.heading("Wins", text="Wins")
        self.my_tree.heading("Draws", text="Draws")
        self.my_tree.heading("Loss", text="Loss")
        self.my_tree.heading("GF (Goals For)", text="GF (Goals For)")
        self.my_tree.heading("GA (Goals Against)", text="GA (Goals Against)")
        self.my_tree.heading("GD (Goals Diff)", text="GD (Goals Diff)")
        self.my_tree.heading("Points", text="Points")

        self.my_tree.tag_configure("oddrow", background="lemon chiffon3", font=("Malgun Gothic", 12))
        self.my_tree.tag_configure("evenrow", background="coral", font=("Malgun Gothic", 12))
        for record in enumerate(self.rows):
            record[1].insert(0, record[0] + 1)
            if record[0] % 2 == 0:
                self.my_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1], tags=("evenrow"))
            else:
                self.my_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1], tags=("oddrow"))
