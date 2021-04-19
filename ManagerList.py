from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from ScreenTemplate import template


class managerlistFrame(template):
    def __init__(self, master):
        super().__init__(master)

        # database connection
        self.managers_list = []
        self.open_a_connection()
        # fixtures
        self.acursor.execute(
            "select p.name, p.nation,p.DOB, p.team, m.hiredate, m.joindate from manager m, participant p where m.mid = p.pid")
        self.managers_list = [manager for manager in self.acursor]
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
        self.managers_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll_bar.set,
                                          style="teamlist.Treeview")
        self.managers_tree.grid(row=0, column=0)

        self.tree_scroll_bar.config(command=self.managers_tree.yview)
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
        self.image_list = []
        for record in enumerate(self.managers_list):
            record = list(record)
            record[1] = list(record[1])
            record[1][2] = record[1][2].date()
            self.image_list.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.png").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.managers_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                          tags=("evenrow"), image=self.image_list[record[0]])
            else:
                self.managers_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                          tags=("oddrow"), image=self.image_list[record[0]])
            self.managers_tree.insert(parent=record[0], index=1, text="", values=['Add to favourites'],
                                      tags=("favourite"))
            self.managers_tree.insert(parent=record[0], index=0, text="", values=["Open this team"], tags=("open"))
