from tkinter import *

from ScreenTemplate import template
from tkinter import ttk
from PIL import ImageTk, Image

class sponsorlistFrame(template):
    def __init__(self, master):
        super().__init__(master)

        self.spon_list = []
        self.open_a_connection()
        # fixtures
        self.acursor.execute(
            "select sname,brandamb from sponsor")
        self.spon_list = [spon for spon in self.acursor]
        self.close_a_connection()

        # match schedule
        self.tree_frame = Frame(self.baseFrame)
        self.tree_frame.place(x=300, y=175, relwidth=0.6, relheight=0.6)
        self.tree_scroll_bar = ttk.Scrollbar(self.tree_frame)
        self.tree_scroll_bar.grid(row=0, column=1, sticky=NS)

        self.treestyle = ttk.Style()
        self.treestyle.theme_use("clam")
        self.treestyle.configure("sponlist.Treeview", background="White", foreground="White", rowheight=65,
                                 font=("@Microsoft YaHei", 15),
                                 fieldbackground="White")
        self.treestyle.map('sponlist.Treeview', background=[('selected', 'coral4')])
        self.treestyle.configure("sponlist.Treeview.Heading", font=("Malgun Gothic", 15, "bold"))
        self.teams_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll_bar.set,
                                       style="sponlist.Treeview")
        self.teams_tree.grid(row=0, column=0)

        self.tree_scroll_bar.config(command=self.teams_tree.yview)
        self.teams_tree['columns'] = ["Sponsor Name", "Brand Owner"]
        self.teams_tree.column("#0", width=250, anchor=CENTER)
        self.teams_tree.column("Sponsor Name", width=350, anchor=CENTER)
        self.teams_tree.column("Brand Owner", width=300, anchor=CENTER)

        self.teams_tree.heading("#0", text="Sponsor Logo", anchor=CENTER)
        self.teams_tree.heading("Sponsor Name", text="Sponsor Name", anchor=CENTER)
        self.teams_tree.heading("Brand Owner", text="Brand Owner", anchor=CENTER)

        self.teams_tree.tag_configure("oddrow", background="White")
        self.teams_tree.tag_configure("evenrow", background="gold2")
        self.image_list_spon = []
        for record in enumerate(self.spon_list):
            record = list(record)
            record[1] = list(record[1])
            self.image_list_spon.append(ImageTk.PhotoImage(
                Image.open(f"Images/{str(record[1][0]).lower()}.jpg").resize((60, 60), Image.ANTIALIAS)))
            if record[0] % 2 == 0:
                self.teams_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                       tags=("evenrow"), image=self.image_list_spon[record[0]])
            else:
                self.teams_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1],
                                       tags=("oddrow"), image=self.image_list_spon[record[0]])