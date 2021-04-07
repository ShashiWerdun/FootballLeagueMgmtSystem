from tkinter import *
from tkinter import ttk

from ScreenTemplate import template


class matchlistFrame(template):

    def __init__(self, master):
        super().__init__(master)
        self.tree_frame = Frame(self.baseFrame)
        self.tree_frame.pack(pady=150)
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.config(command=self.my_tree.yview)
        self.usable_frame = Frame(self.tree_frame)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="cornsilk3", foreground="black", rowheight=27,
                             fieldbackground="cornsilk3")
          self.style.map('Treeview',background=[('selected','coral4')])

          self.my_tree.pack()

          self.my_tree['columns'] = ("Team1", "Team2", "Score1-Score2", "Time-Date")
          self.my_tree.column("#0", width=0, stretch=NO)
          self.my_tree.column("Team1", width=200)
          self.my_tree.column("Team2", width=200)
          self.my_tree.column("Score1-Score2", width=200)
          self.my_tree.column("Time-Date", width=170)

          self.my_tree.heading("#0", text="")
          self.my_tree.heading("Team1", text="Team1")
          self.my_tree.heading("Team2", text="Team2")
          self.my_tree.heading("Score1-Score2", text="Score1-Score2")
          self.my_tree.heading("Time-Date", text="Time-Date")

          self.data = [
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67],
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67],
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67],
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67],
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67],
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67],
              [1, 2, 34, 5],
              [2, 4, 5, 67],
              [3, 45, 56, 67]

                 ]

          self.count=0
          for record in self.data:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=(record[0], record[1], record[2], record[3]))
                self.count += 1


