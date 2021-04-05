from tkinter import *


class matchlistFrame:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(pady=90)
        self.my_canvas = Canvas(self.frame, bg="cornsilk3", width=500, height=500, scrollregion=(0, 0, 2000, 2000))
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.my_canvas.yview)
        self.my_canvas.config(width=500, height=500)
        self.my_canvas.config(yscrollcommand=self.vbar.set)
        self.my_canvas.pack()


        self.my_canvas.create_text(50, 20, text="TEAM1", font="Times")
        self.my_canvas.create_line(100, 0, 100, 2000, fill="coral4")
        self.my_canvas.create_text(145, 20, text="TEAM2", font="Times")
        self.my_canvas.create_line(195, 0, 195, 2000, fill="coral4")
        self.my_canvas.create_text(270, 20, text="TIME-DATE", font="Times")
        self.my_canvas.create_line(350, 0, 350, 2000, fill="coral4")
        self.my_canvas.create_text(420, 20, text="SCORE1-SCORE2", font="Times")
        self.my_canvas.create_line(0, 40, 500, 40, fill="coral4")