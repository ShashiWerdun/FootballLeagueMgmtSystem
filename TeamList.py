from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from ScreenTemplate import template


class teamlistFrame(template):
    def __init__(self, master):
        super().__init__(master)

        # database connection
        self.team_list = []
        self.open_a_connection()
        # fixtures
        self.acursor.execute(
            "select tname, ceo, homeground from team")
        self.team_list = [team for team in self.acursor]
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
        self.teams_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll_bar.set,
                                       style="teamlist.Treeview")
        self.teams_tree.grid(row=0, column=0)

        self.tree_scroll_bar.config(command=self.teams_tree.yview)
        self.teams_tree['columns'] = ["Team Name", "CEO", "Home Stadium"]
        self.teams_tree.column("#0", width=200, anchor=CENTER)
        self.teams_tree.column("Team Name", width=300, anchor=W)
        self.teams_tree.column("CEO", width=250, anchor=W)
        self.teams_tree.column("Home Stadium", width=350, anchor=W)

        self.teams_tree.heading("#0", text="Team Logo", anchor=CENTER)
        self.teams_tree.heading("Team Name", text="Team Name", anchor=W)
        self.teams_tree.heading("CEO", text="CEO", anchor=W)
        self.teams_tree.heading("Home Stadium", text="Home Stadium", anchor=W)

        self.teams_tree.tag_configure("oddrow", background="White")
        self.teams_tree.tag_configure("evenrow", background="gold2")
        self.teams_tree.tag_configure("open", background="pink")
        self.teams_tree.tag_configure("favourite", background="red")
        self.image_list = []
        for record in enumerate(self.team_list):
            record = list(record)
            record[1] = list(record[1])
            self.image_list.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.jpg").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.teams_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                       tags=("evenrow"), image=self.image_list[record[0]])
            else:
                self.teams_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                       tags=("oddrow"), image=self.image_list[record[0]])
            self.teams_tree.insert(parent=record[0], index=1, text="", values=['Add to favourites'], tags=("favourite"))
            self.teams_tree.insert(parent=record[0], index=0, text="", values=["Open this team"], tags=("open"))
