from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from ScreenTemplate import template


class pointsTableFrame(template):

    def __init__(self, master):
        self.bgimage = ImageTk.PhotoImage(
            Image.open("Images/bgnew.jpg").resize((master.winfo_screenwidth(), master.winfo_screenheight()),
                                                  Image.ANTIALIAS))
        super().__init__(master, self.bgimage)
        self.tree_frame = Frame(self.baseFrame)
        self.tree_frame.pack(pady=150)
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        self.usable_frame = Frame(self.tree_frame)

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

        self.data = [
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 0],
            [2, 4, 5, 67, 56, 77, 665, 4, 8, 90],
            [3, 45, 56, 67, 765, 56, 78, 765, 900, 567],
            [3, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [3, 2, 34, 456, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 224, 6, 7, 89, 345, 5, 6],
            [1, 234, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 3, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 46, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 82, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 34, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 69, 345, 5, 6],
            [1, 2, 34, 5, 34, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 345, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 8556, 345, 5, 6],
            [10, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 23, 6, 7, 89, 345, 5, 6],
            [1, 2, 34, 5, 6, 7, 89, 334, 5, 6]

        ]

        self.my_tree.tag_configure("oddrow", background="lemon chiffon3", font=("Malgun Gothic", 12))
        self.my_tree.tag_configure("evenrow", background="coral", font=("Malgun Gothic", 12))
        self.count = 0
        for record in enumerate(self.data):
            if record[0] % 2 == 0:
                self.my_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1], tags=("evenrow"))
            else:
                self.my_tree.insert(parent="", index=END, iid=record[0], text="", values=record[1], tags=("oddrow"))
            self.count += 1
