import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from ScreenTemplate import template


class HomeScreenFrameGen(template):

    def __init__(self, master):
        super().__init__(master)

        # required
        font = tkFont.Font(family="Courier New Greek", size=20)

        # donot use this frame for inserting any widget. You should use another variable called usable_frame
        self.main_frame = Frame(self.baseFrame)
        self.main_canvas = Canvas(self.main_frame)
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.main_scroll_bar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.main_canvas.yview)
        self.main_scroll_bar.pack(side=RIGHT, fill=Y)
        self.main_canvas.configure(yscrollcommand=self.main_scroll_bar.set)
        self.main_canvas.bind('<Configure>',
                              lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        self.usable_frame = Frame(self.main_canvas)
        self.main_canvas.create_window((0, 0), window=self.usable_frame, anchor=NW, width=self.screenwidth,
                                       height=self.screenheight)

        # BG image
        self.bgimg = ImageTk.PhotoImage(
            Image.open("Images\home_bg.jpg").resize((self.screenwidth, self.screenheight), Image.ANTIALIAS))
        Label(self.usable_frame, image=self.bgimg).place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.usable_frame,
              text="Upcoming Matches",
              font=("Constantia", 16, "bold")).place(x=7, y=100)
        self.profileimg = ImageTk.PhotoImage(Image.open("Images\manprofilepic.png").resize((40, 40), Image.ANTIALIAS))
        self.ButtonStyleForProf = ttk.Style(master)
        self.ButtonStyleForProf.configure("Prof.TButton", background="Black", foreground="Black",
                                          font=("Lucida Console", 20, "bold"))
        self.profilebutton = ttk.Button(self.usable_frame,
                                        image=self.profileimg,
                                        text="Profile",
                                        compound=TOP,
                                        style="Prof.TButton")
        self.profilebutton.place(anchor=NE, x=self.usable_frame.winfo_screenwidth() - 40, y=15)
        self.logoutimg = ImageTk.PhotoImage(Image.open("Images\\logout.png").resize((40, 40), Image.ANTIALIAS))
        self.logoutbutton = ttk.Button(self.usable_frame, text="Logout", image=self.logoutimg, compound=LEFT,
                                       style="Prof.TButton")
        self.logoutbutton.place(x=10, y=15)

        # Points Table
        self.points_table_button = Button(self.usable_frame, text="Points Table", borderwidth=5, relief="ridge",
                                          font=font, bg="lemon chiffon")
        self.points_table_button.place(x=200, y=300, relwidth=0.75)

        # Fixtures
        self.fixture_main_frame = Frame(self.usable_frame)
        self.fixture_main_frame.place(x=7, y=130, relwidth=0.97, relheight=0.175)
        self.fixture_canvas = Canvas(self.fixture_main_frame)
        self.fixture_canvas.place(x=0, y=0, relwidth=1)
        self.fixture_scroll_bar = ttk.Scrollbar(self.fixture_main_frame, orient=HORIZONTAL,
                                                command=self.fixture_canvas.xview)
        self.fixture_scroll_bar.place(anchor=SW, x=0, y=150, relwidth=1)
        self.fixture_canvas.configure(xscrollcommand=self.fixture_scroll_bar.set)
        self.fixture_canvas.bind('<Configure>',
                                 lambda e: self.fixture_canvas.configure(scrollregion=self.fixture_canvas.bbox("all")))
        self.fixture_Frame = Frame(self.fixture_canvas)
        self.fixture_canvas.create_window((0, 0), window=self.fixture_Frame, anchor="nw")
        for option in [("Manchester United FC", "Liverpool", "03-04-2021", "7:30PM IST"),
                       ("Chelsa FC", "Arsenel", "04-04-2021", "7:00 PST"),
                       ("Manchester City FC", "Tottenham", "05-04-2021", "6:00 PST"),
                       ("Leicester City", "Leeds United", "06-04-2021", "5:00 WST"),
                       ("Manchester United FC", "Liverpool", "03-04-2021", "7:30PM IST"),
                       ("Chelsa FC", "Arsenel", "04-04-2021", "7:00 PST"),
                       ("Manchester City FC", "Tottenham", "05-04-2021", "6:00 PST"),
                       ("Leicester City", "Leeds United", "06-04-2021", "5:00 WST"),
                       ("Manchester United FC", "Liverpool", "03-04-2021", "7:30PM IST"),
                       ("Chelsa FC", "Arsenel", "04-04-2021", "7:00 PST"),
                       ("Manchester City FC", "Tottenham", "05-04-2021", "6:00 PST"),
                       ("Leicester City", "Leeds United", "06-04-2021", "5:00 WST"),
                       ("Manchester United FC", "Liverpool", "03-04-2021", "7:30PM IST"),
                       ("Chelsa FC", "Arsenel", "04-04-2021", "7:00 PST"),
                       ("Manchester City FC", "Tottenham", "05-04-2021", "6:00 PST"),
                       ("Leicester City", "Leeds United", "06-04-2021", "5:00 WST")]:
            Button(self.fixture_Frame,
                   text=f"{option[0]}\nVs\n{option[1]}\nOn {option[2]} {option[3]}",
                   font=("Comic Sans MS", 14),
                   bg="tomato",
                   width=25,
                   pady=4,
                   borderwidth=0).pack(side=LEFT, padx=5)
        # Fixtures done

        # match schedule
        self.match_tree_frame = Frame(self.usable_frame)
        self.match_tree_frame.place(x=125, y=400, relwidth=0.825)
        self.tree_scroll_bar = ttk.Scrollbar(self.match_tree_frame)
        self.tree_scroll_bar.grid(row=1, column=4, sticky=NS)
        Label(self.main_frame,
              text="All Matches",
              font=("Constantia", 16, "bold"), borderwidth=0, width=10).place(x=125, y=373)

        self.treestyle = ttk.Style()
        # self.treestyle.theme_use("default")
        self.treestyle.configure("Treeview", background="White", foreground="White", rowheight=50,
                                 font=("Malgun Gothic", 10),
                                 fieldbackground="White")
        self.treestyle.map('Treeview', background=[('selected', "#0AFFEF")])
        self.matchschedule = ttk.Treeview(self.match_tree_frame, yscrollcommand=self.tree_scroll_bar.set, )
        self.matchschedule.grid(row=1, column=0, columnspan=4)

        self.tree_scroll_bar.config(command=self.matchschedule.yview)
        self.matchschedule['columns'] = ["MatchTeam1", "MatchTeam2", "Timeandday", "Stadium"]
        self.matchschedule.column("#0", width=0, stretch=NO)
        self.matchschedule.column("MatchTeam1", width=350, anchor=W)
        self.matchschedule.column("MatchTeam2", width=350, anchor=W)
        self.matchschedule.column("Timeandday", width=350, anchor=CENTER)
        self.matchschedule.column("Stadium", width=200, anchor=CENTER)

        self.matchschedule.heading("#0", text="")
        self.matchschedule.heading("MatchTeam1", text="Team1", anchor=W)
        self.matchschedule.heading("MatchTeam2", text="Team2", anchor=W)
        self.matchschedule.heading("Timeandday", text="When", anchor=CENTER)
        self.matchschedule.heading("Stadium", text="Location", anchor=CENTER)

        schedulelist = [("Manchester United FC", "Liverpool", "03-04-2021 - 7:30PM IST", "Stadium1"),
                        ("Chelsa FC", "Arsenel", "04-04-2021 - 7:00 PST", "Stadium2"),
                        ("Manchester City FC", "Tottenham", "05-04-2021 - 6:00 PST", "Stadium3"),
                        ("Leicester City", "Leeds United", "06-04-2021 - 5:00 WST", "Stadium4"),
                        ("Manchester United FC", "Liverpool", "03-04-2021 - 7:30PM IST", "Stadium1"),
                        ("Chelsa FC", "Arsenel", "04-04-2021 - 7:00 PST", "Stadium2"),
                        ("Manchester City FC", "Tottenham", "05-04-2021 - 6:00 PST", "Stadium3"),
                        ("Leicester City", "Leeds United", "06-04-2021 - 5:00 WST", "Stadium4"),
                        ("Manchester United FC", "Liverpool", "03-04-2021 - 7:30PM IST", "Stadium1"),
                        ("Chelsa FC", "Arsenel", "04-04-2021 - 7:00 PST", "Stadium2"),
                        ("Manchester City FC", "Tottenham", "05-04-2021 - 6:00 PST", "Stadium3"),
                        ("Leicester City", "Leeds United", "06-04-2021 - 5:00 WST", "Stadium4"),
                        ("Manchester United FC", "Liverpool", "03-04-2021 - 7:30PM IST", "Stadium1"),
                        ("Chelsa FC", "Arsenel", "04-04-2021 - 7:00 PST", "Stadium2"),
                        ("Manchester City FC", "Tottenham", "05-04-2021 - 6:00 PST", "Stadium3"),
                        ("Leicester City", "Leeds United", "06-04-2021 - 5:00 WST", "Stadium4")]

        match_font = tkFont.Font(family="Calibri Light", size=16)
        self.matchschedule.tag_configure("oddrow", background="White", font=match_font)
        self.matchschedule.tag_configure("evenrow", background="gold2", font=match_font)
        for record in enumerate(schedulelist):
            if record[0] % 2 == 0:
                self.matchschedule.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                          tags=("evenrow"))
            else:
                self.matchschedule.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                          tags=("oddrow"))

        for _ in range(4):
            self.match_tree_frame.columnconfigure(_, minsize=300)

        self.teams_list_button = Button(self.match_tree_frame, text="Teams", font=font, borderwidth=0,
                                        background="tomato")
        self.teams_list_button.grid(row=2, column=0, padx=5, pady=5, sticky=EW)
        self.players_list_button = Button(self.match_tree_frame, text="All Players", font=font, borderwidth=0,
                                          background="tomato")
        self.players_list_button.grid(row=2, column=1, padx=5, pady=5, sticky=EW)
        self.managers_list_button = Button(self.match_tree_frame, text="Club Managers", font=font, borderwidth=0,
                                           background="tomato")
        self.managers_list_button.grid(row=2, column=2, padx=5, pady=5, sticky=EW)
        self.sponsors_list_button = Button(self.match_tree_frame, text="League Sponsors", font=font, borderwidth=0,
                                           background="tomato")
        self.sponsors_list_button.grid(row=2, column=3, padx=5, pady=5, sticky=EW)

        self.main_frame.pack(fill=BOTH, expand=1, ipadx=10, ipady=10)
