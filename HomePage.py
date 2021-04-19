import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from ScreenTemplate import template


class HomeScreenFrameGen(template):

    def __init__(self, master):
        super().__init__(master)

        # database connection
        self.fixtures_list = []
        self.match_schedule_list = []
        self.open_a_connection()
        # fixtures
        self.acursor.execute(
            "select stname, mdate, time, m1.tname, host from match m, match_team m1 where m.mid=m1.mid and m.host!=m1.tname and m.tot_goals is NULL")
        self.fixtures_list = [match for match in self.acursor]
        # schedule
        self.acursor.execute(
            "select m1.tname, host, mdate, time, stname, m.mid from match m, match_team m1 where m.mid=m1.mid and m.host!=m1.tname")
        self.match_schedule_list = [match for match in self.acursor]
        self.close_a_connection()

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
              font=("Constantia", 16, "bold")).place(x=7, y=90)
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
        self.fixture_main_frame.place(x=7, y=120, relwidth=0.97, relheight=0.2)
        self.fixture_canvas = Canvas(self.fixture_main_frame)
        self.fixture_canvas.place(x=0, y=0, relwidth=1)
        self.fixture_scroll_bar = ttk.Scrollbar(self.fixture_main_frame, orient=HORIZONTAL,
                                                command=self.fixture_canvas.xview)
        self.fixture_scroll_bar.place(anchor=SW, x=0, y=175, relwidth=1)
        self.fixture_canvas.configure(xscrollcommand=self.fixture_scroll_bar.set)
        self.fixture_canvas.bind('<Configure>',
                                 lambda e: self.fixture_canvas.configure(scrollregion=self.fixture_canvas.bbox("all")))
        self.fixture_Frame = Frame(self.fixture_canvas)
        self.fixture_canvas.create_window((0, 0), window=self.fixture_Frame, anchor="nw")
        self.fixstyle = ttk.Style()
        self.fixstyle.theme_use("clam")
        self.fixstyle.configure("fixstyle.TButton", font=("Comic Sans MS", 10), background="thistle3", width=25, pady=4)
        self.imageslist = []
        for option in self.fixtures_list:
            teamA = str(option[3]).lower()
            teamB = str(option[4]).lower()
            self.logo1 = Image.open(f"Images\{teamA}.jpeg").resize((100, 100), Image.ANTIALIAS)
            self.logo2 = Image.open(f"Images\{teamB}.jpeg").resize((100, 100), Image.ANTIALIAS)
            self.fiximage = Image.new('RGB', (200, 100), (250, 250, 250))
            self.fiximage.paste(self.logo1, (0, 0))
            self.fiximage.paste(self.logo2, (100, 0))
            self.imageslist.append(self.logo1)
            self.imageslist.append(self.logo2)
            self.imageslist.append(self.fiximage)
            self.tkimage = ImageTk.PhotoImage(self.fiximage)
            ttk.Button(self.fixture_Frame,
                       text=f"On {str(option[1].date())}, {option[2]}\nat {option[0]}",
                       style="fixstyle.TButton",
                       image=self.tkimage, compound=TOP).pack(side=LEFT, padx=5, ipadx=100)
        # Fixtures done

        # match schedule
        self.match_tree_frame = Frame(self.usable_frame)
        self.match_tree_frame.place(x=125, y=400, relwidth=0.825)
        self.tree_scroll_bar = ttk.Scrollbar(self.match_tree_frame)
        self.tree_scroll_bar.grid(row=1, column=4, sticky=NS)
        Label(self.usable_frame,
              text="All Matches",
              font=("Constantia", 16, "bold"), borderwidth=0, width=10).place(x=125, y=373)

        self.treestyle = ttk.Style()
        self.treestyle.theme_use("clam")
        self.treestyle.configure("homescreen.Treeview", background="White", foreground="White", rowheight=35,
                                 font=("Malgun Gothic", 10),
                                 fieldbackground="White")
        self.treestyle.map('homescreen.Treeview', background=[('selected', 'coral4')])
        self.treestyle.configure("homescreen.Treeview.Heading", font=("Malgun Gothic", 14, "bold"))
        self.matchschedule = ttk.Treeview(self.match_tree_frame, yscrollcommand=self.tree_scroll_bar.set,
                                          style="homescreen.Treeview")
        self.matchschedule.grid(row=1, column=0, columnspan=4)

        self.tree_scroll_bar.config(command=self.matchschedule.yview)
        self.matchschedule['columns'] = ["MatchTeam1", "MatchTeam2", "Day", "Time", "Stadium"]
        self.matchschedule.column("#0", width=0, stretch=NO)
        self.matchschedule.column("MatchTeam1", width=350, anchor=W)
        self.matchschedule.column("MatchTeam2", width=350, anchor=W)
        self.matchschedule.column("Day", width=175, anchor=CENTER)
        self.matchschedule.column("Time", width=175, anchor=CENTER)
        self.matchschedule.column("Stadium", width=200, anchor=CENTER)

        self.matchschedule.heading("#0", text="")
        self.matchschedule.heading("MatchTeam1", text="Team1", anchor=W)
        self.matchschedule.heading("MatchTeam2", text="Team2", anchor=W)
        self.matchschedule.heading("Day", text="Date", anchor=CENTER)
        self.matchschedule.heading("Time", text="Time", anchor=CENTER)
        self.matchschedule.heading("Stadium", text="Location", anchor=CENTER)

        match_font = tkFont.Font(family="Calibri Light", size=16)
        self.matchschedule.tag_configure("oddrow", background="White", font=match_font)
        self.matchschedule.tag_configure("evenrow", background="gold2", font=match_font)
        for record in enumerate(self.match_schedule_list):
            record = list(record)
            record[1] = list(record[1])
            mid = record[1][-1]
            record[1] = record[1][0:-1]
            record[1][2] = record[1][2].date()
            if record[0] % 2 == 0:
                self.matchschedule.insert(parent="", index=END, iid=mid, text="", values=record[1],
                                          tags=("evenrow"))
            else:
                self.matchschedule.insert(parent="", index=END, iid=mid, text="", values=record[1],
                                          tags=("oddrow"))

        for _ in range(4):
            self.match_tree_frame.columnconfigure(_, minsize=300)

        bottom_button_font = tkFont.Font(family="Courier New Greek", size=16, weight="bold")

        self.teams_list_button = Button(self.match_tree_frame, text="Teams", font=bottom_button_font, borderwidth=3,
                                        background="tan1", relief="raised")
        self.teams_list_button.grid(row=2, column=0, padx=5, pady=5, sticky=EW)
        self.players_list_button = Button(self.match_tree_frame, text="All Players", font=bottom_button_font,
                                          borderwidth=3, relief="raised",
                                          background="tan1")
        self.players_list_button.grid(row=2, column=1, padx=5, pady=5, sticky=EW)
        self.managers_list_button = Button(self.match_tree_frame, text="Club Managers", font=bottom_button_font,
                                           borderwidth=3, relief="raised",
                                           background="tan1")
        self.managers_list_button.grid(row=2, column=2, padx=5, pady=5, sticky=EW)
        self.sponsors_list_button = Button(self.match_tree_frame, text="League Sponsors", font=bottom_button_font,
                                           borderwidth=3, relief="raised",
                                           background="tan1")
        self.sponsors_list_button.grid(row=2, column=3, padx=5, pady=5, sticky=EW)

        self.main_frame.pack(fill=BOTH, expand=1, ipadx=10, ipady=10)

    def place_profile_button(self):
        self.profilebutton.place(anchor=NE, x=self.usable_frame.winfo_screenwidth() - 40, y=15)
