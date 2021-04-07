from tkinter import *

from ScreenTemplate import template


class sponsorlistFrame(template):
    def __init__(self, master):
        super().__init__(master)
        self.frame = Frame(self.baseFrame)
        self.frame.pack(pady=90)
        self.my_canvas = Canvas(self.frame, bg="cornsilk3", width=500, height=500, scrollregion=(0, 0, 2000, 2000))
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.my_canvas.yview)
        self.my_canvas.config(width=500, height=500)
        self.my_canvas.config(yscrollcommand=self.vbar.set)
        self.my_canvas.pack()


        self.my_canvas.create_text(85, 20, text="SPONSORER NAME", font="Times")
        self.my_canvas.create_line(170, 0, 170, 2000, fill="coral4")
        self.my_canvas.create_text(230, 20, text="LOGO", font="Times")
        self.my_canvas.create_line(290, 0, 290, 2000, fill="coral4")
        self.my_canvas.create_text(405, 20, text="BRAND AMBASSADOR", font="Times")
        self.my_canvas.create_line(0, 40, 500, 40, fill="coral4")
