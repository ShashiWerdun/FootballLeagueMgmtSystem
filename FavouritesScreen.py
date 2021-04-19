from tkinter import *
from tkinter import font
from tkinter import ttk

from PIL import ImageTk, Image

from ScreenTemplate import template


class favouritesScreenframe(template):
    def __init__(self, master, uid=None):
        if uid is not None:
            super().__init__(master)

            # donot use this frame for inserting any widget. You should use another variable called usable_frame
            self.main_canvas = Canvas(self.baseFrame)
            self.main_canvas.place(x=200, y=0, relwidth=0.76, relheight=1)
            self.main_scroll_bar = ttk.Scrollbar(self.baseFrame, orient=VERTICAL, command=self.main_canvas.yview)
            self.main_scroll_bar.pack(side=RIGHT, fill=Y)
            self.main_canvas.configure(yscrollcommand=self.main_scroll_bar.set)
            self.main_canvas.bind('<Configure>',
                                  lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
            self.usable_frame = Frame(self.main_canvas)
            self.main_canvas.create_window((0, 0), window=self.usable_frame, anchor=NW)

            # common style for favourites tree views
            self.treestyle = ttk.Style()
            self.treestyle.theme_use("clam")
            self.treestyle.configure("favourites.Treeview", background="White", foreground="White", rowheight=65,
                                     font=("@Microsoft YaHei", 12),
                                     fieldbackground="White")
            self.treestyle.map('favourites.Treeview', background=[('selected', 'coral4')])
            self.treestyle.configure("favourites.Treeview.Heading", font=("Malgun Gothic", 15, "bold"))
            self.header_font = font.Font(family="Constantia", size=22, weight="bold")

            # FAVOURITE TEAMS
            # favourite teams label
            Label(self.usable_frame,
                  text="Your favourite Teams", font=self.header_font, borderwidth=0).pack()
            # treeview
            self.fav_team_frame = Frame(self.usable_frame)
            self.fav_team_frame.pack()
            self.fav_team_scroll_bar = ttk.Scrollbar(self.fav_team_frame)
            self.fav_team_scroll_bar.grid(row=0, column=1, sticky=NS)
            self.teams_tree = ttk.Treeview(self.fav_team_frame, yscrollcommand=self.fav_team_scroll_bar.set,
                                           style="favourites.Treeview")
            self.teams_tree.grid(row=0, column=0)

            self.fav_team_scroll_bar.config(command=self.teams_tree.yview)
            self.teams_tree['columns'] = ["Team Name", "CEO", "Home Stadium"]
            self.teams_tree.column("#0", width=200, anchor=CENTER)
            self.teams_tree.column("Team Name", width=330, anchor=W)
            self.teams_tree.column("CEO", width=265, anchor=W)
            self.teams_tree.column("Home Stadium", width=350, anchor=W)

            self.teams_tree.heading("#0", text="Team Logo", anchor=CENTER)
            self.teams_tree.heading("Team Name", text="Team Name", anchor=W)
            self.teams_tree.heading("CEO", text="CEO", anchor=W)
            self.teams_tree.heading("Home Stadium", text="Home Stadium", anchor=W)

            self.teams_tree.tag_configure("oddrow", background="White")
            self.teams_tree.tag_configure("evenrow", background="gold2")
            self.teams_tree.tag_configure("open", background="pink")
            self.teams_tree.tag_configure("favourite", background="red")

            # FAVOURITE PLAYERS
            # favourite players label
            Label(self.usable_frame,
                  text="Your favourite Players", font=self.header_font, borderwidth=0).pack()
            # treeview
            self.fav_players_frame = Frame(self.usable_frame)
            self.fav_players_frame.pack()
            self.fav_players_scroll_bar = ttk.Scrollbar(self.fav_players_frame)
            self.fav_players_scroll_bar.grid(row=0, column=1, sticky=NS)

            self.players_tree = ttk.Treeview(self.fav_players_frame, yscrollcommand=self.fav_players_scroll_bar.set,
                                             style="favourites.Treeview")
            self.players_tree.grid(row=0, column=0)

            self.fav_players_scroll_bar.config(command=self.players_tree.yview)
            self.players_tree['columns'] = ["Player Name", "Rank", "Date of Birth", "Nation", "Team", "MPPOS"]
            self.players_tree.column("#0", width=150, anchor=CENTER)
            self.players_tree.column("Player Name", width=280, anchor=W)
            self.players_tree.column("Rank", width=60, anchor=W)
            self.players_tree.column("Date of Birth", width=150, anchor=W)
            self.players_tree.column("Nation", width=140, anchor=W)
            self.players_tree.column("Team", width=195, anchor=W)
            self.players_tree.column("MPPOS", width=170, anchor=W)

            self.players_tree.heading("#0", text="Player Image", anchor=CENTER)
            self.players_tree.heading("Player Name", text="Player Name", anchor=W)
            self.players_tree.heading("Rank", text="Rank", anchor=W)
            self.players_tree.heading("Date of Birth", text="Date of Birth", anchor=W)
            self.players_tree.heading("Nation", text="Nation", anchor=W)
            self.players_tree.heading("Team", text="Team", anchor=W)
            self.players_tree.heading("MPPOS", text="Most played", anchor=W)

            self.players_tree.tag_configure("oddrow", background="White")
            self.players_tree.tag_configure("evenrow", background="gold2")
            self.players_tree.tag_configure("open", background="pink")
            self.players_tree.tag_configure("favourite", background="red")

            # FAVOURITE MANAGERS
            # favourite managers label
            Label(self.usable_frame,
                  text="Your favourite Managers", font=self.header_font, borderwidth=0).pack()
            # treeview
            self.fav_managers_frame = Frame(self.usable_frame)
            self.fav_managers_frame.pack()
            self.fav_managers_scroll_bar = ttk.Scrollbar(self.fav_managers_frame)
            self.fav_managers_scroll_bar.grid(row=0, column=1, sticky=NS)

            self.managers_tree = ttk.Treeview(self.fav_managers_frame, yscrollcommand=self.fav_managers_scroll_bar.set,
                                              style="favourites.Treeview")
            self.managers_tree.grid(row=0, column=0)

            self.fav_managers_scroll_bar.config(command=self.managers_tree.yview)
            self.managers_tree['columns'] = ["Manager Name", "Nationality", "Date of Birth", "Team", "Hire date",
                                             "Join date"]
            self.managers_tree.column("#0", width=150, anchor=CENTER)
            self.managers_tree.column("Manager Name", width=250, anchor=W)
            self.managers_tree.column("Nationality", width=60, anchor=W)
            self.managers_tree.column("Date of Birth", width=150, anchor=W)
            self.managers_tree.column("Team", width=195, anchor=W)
            self.managers_tree.column("Hire date", width=170, anchor=W)
            self.managers_tree.column("Join date", width=170, anchor=W)

            self.managers_tree.heading("#0", text="Manager Image", anchor=CENTER)
            self.managers_tree.heading("Manager Name", text="Manager Name", anchor=W)
            self.managers_tree.heading("Date of Birth", text="Date of Birth", anchor=W)
            self.managers_tree.heading("Nationality", text="Nationality", anchor=W)
            self.managers_tree.heading("Team", text="Team", anchor=W)
            self.managers_tree.heading("Hire date", text="Hire date", anchor=W)
            self.managers_tree.heading("Join date", text="Join date", anchor=W)

            self.managers_tree.tag_configure("oddrow", background="White")
            self.managers_tree.tag_configure("evenrow", background="gold2")
            self.managers_tree.tag_configure("open", background="pink")
            self.managers_tree.tag_configure("favourite", background="red")

            # get data and display
            self.refresh_data(uid)
            self.refresh_display()

    def refresh_data(self, uid):
        # start database connection
        self.open_a_connection()

        # data for favourite teams list
        self.fav_team_list = []
        self.acursor.execute(
            f"select tname, ceo, homeground from team where tname in (select tname from fav_team where fid = {uid})")
        self.fav_team_list = [team for team in self.acursor]

        # data for favourite managers list
        self.fav_managers_list = []
        self.acursor.execute(
            f"select p.name, p.nation,p.DOB, p.team, m.hiredate, m.joindate from manager m, participant p where m.mid = p.pid and m.mid in (select pid from fav_team where fid = {uid})")
        self.fav_managers_list = [manager for manager in self.acursor]

        # data for favourite players list
        self.fav_players_list = []
        self.acursor.execute(
            f"select name, rank, DOB, nation, team, MPPOS from participant pa, player p where p.pid = pa.pid and p.pid in (select pid from fav_participant where fid = {uid})")
        self.fav_players_list = [player for player in self.acursor]

        # close database connection
        self.close_a_connection()

    def refresh_display(self):

        # clear all trees
        self.managers_tree.delete(*self.managers_tree.get_children())
        self.players_tree.delete(*self.players_tree.get_children())
        self.teams_tree.delete(*self.teams_tree.get_children())

        # display favourite managers list
        self.fav_managers_image_list = []
        for record in enumerate(self.fav_managers_list):
            record = list(record)
            record[1] = list(record[1])
            record[1][2] = record[1][2].date()
            self.fav_managers_image_list.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.png").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.managers_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                          tags=("evenrow"), image=self.fav_managers_image_list[record[0]])
            else:
                self.managers_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                          tags=("oddrow"), image=self.fav_managers_image_list[record[0]])
            self.managers_tree.insert(parent=record[0], index=1, text="", values=['Remove from favourites'],
                                      tags=("favourite"))
            self.managers_tree.insert(parent=record[0], index=0, text="", values=["Open this team"], tags=("open"))

        # display favourite players list
        self.fav_players_image_list = []
        for record in enumerate(self.fav_players_list):
            record = list(record)
            record[1] = list(record[1])
            record[1][2] = record[1][2].date()
            self.fav_players_image_list.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.png").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.players_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                         tags=("evenrow"), image=self.fav_players_image_list[record[0]])
            else:
                self.players_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                         tags=("oddrow"), image=self.fav_players_image_list[record[0]])
            self.players_tree.insert(parent=record[0], index=1, text="", values=['Remove from favourites'],
                                     tags=("favourite"))
            self.players_tree.insert(parent=record[0], index=0, text="", values=["Open this player"], tags=("open"))

        # display favourite teams list
        self.fav_teams_image_list = []
        for record in enumerate(self.fav_team_list):
            record = list(record)
            record[1] = list(record[1])
            self.fav_teams_image_list.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.jpeg").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.teams_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                       tags=("evenrow"), image=self.fav_teams_image_list[record[0]])
            else:
                self.teams_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                       tags=("oddrow"), image=self.fav_teams_image_list[record[0]])
            self.teams_tree.insert(parent=record[0], index=1, text="", values=['Remove from favourites'],
                                   tags=("favourite"))
            self.teams_tree.insert(parent=record[0], index=0, text="", values=["Open this team"], tags=("open"))
