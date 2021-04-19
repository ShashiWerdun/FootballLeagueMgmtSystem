from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from ScreenTemplate import template


class playerlistFrame(template):
    def __init__(self, master):
        super().__init__(master)

        # database connection
        self.players_list = []
        self.open_a_connection()
        # fixtures
        self.acursor.execute(
            "select name, rank, DOB, nation, team, MPPOS from participant pa, player p where p.pid = pa.pid")
        self.players_list = [player for player in self.acursor]
        self.close_a_connection()
        # match schedule
        self.tree_frame = Frame(self.baseFrame)
        self.tree_frame.place(x=225, y=100, relwidth=0.728, relheight=0.82)
        self.tree_scroll_bar = ttk.Scrollbar(self.tree_frame)
        self.tree_scroll_bar.grid(row=0, column=1, sticky=NS)

        self.treestyle = ttk.Style()
        self.treestyle.theme_use("clam")
        self.treestyle.configure("teamlist.Treeview", background="White", foreground="White", rowheight=65,
                                 font=("@Microsoft YaHei", 12),
                                 fieldbackground="White")
        self.treestyle.map('teamlist.Treeview', background=[('selected', 'coral4')])
        self.treestyle.configure("teamlist.Treeview.Heading", font=("Malgun Gothic", 15, "bold"))
        self.players_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll_bar.set,
                                         style="teamlist.Treeview")
        self.players_tree.grid(row=0, column=0)

        self.tree_scroll_bar.config(command=self.players_tree.yview)
        self.players_tree['columns'] = ["Player Name", "Rank", "Date of Birth", "Nation", "Team", "MPPOS"]
        self.players_tree.column("#0", width=150, anchor=CENTER)
        self.players_tree.column("Player Name", width=250, anchor=W)
        self.players_tree.column("Rank", width=60, anchor=W)
        self.players_tree.column("Date of Birth", width=150, anchor=W)
        self.players_tree.column("Nation", width=120, anchor=W)
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
        self.image_list = []
        for record in enumerate(self.players_list):
            record = list(record)
            record[1] = list(record[1])
            record[1][2] = record[1][2].date()
            self.image_list.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.png").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.players_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                         tags=("evenrow"), image=self.image_list[record[0]])
            else:
                self.players_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                         tags=("oddrow"), image=self.image_list[record[0]])
