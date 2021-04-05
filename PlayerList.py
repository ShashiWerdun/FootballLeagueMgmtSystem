from tkinter import *

class playerlistFrame:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(pady=90)
        self.my_canvas = Canvas(self.frame, bg="cornsilk3", width=720, height=500, scrollregion=(0, 0, 2000, 2000))
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.my_canvas.yview)
        self.my_canvas.config(width=720,height=500)
        self.my_canvas.config(yscrollcommand=self.vbar.set)
        self.my_canvas.pack()
        self.img = PhotoImage(file="Images\Messi1.png")
        self.img1 = PhotoImage(file="Images\R2.png")
        
        self.my_canvas.create_text(63,20,text="NAME",font="Times")
        self.my_canvas.create_line(125,0,125,2000,fill="coral4")
        self.my_canvas.create_text(160,20,text="AGE",font="Times")
        self.my_canvas.create_line(195,0,195,2000,fill="coral4")
        self.my_canvas.create_text(242,20,text="GENDER",font="Times")
        self.my_canvas.create_line(295,0,295,2000,fill="coral4")
        self.my_canvas.create_text(352,20,text="NATION",font="Times")
        self.my_canvas.create_line(410,0,410,2000,fill="coral4")
        self.my_canvas.create_text(476,20,text="TEAM",font="Times")
        self.my_canvas.create_line(550,0,550,2000,fill="coral4")
        self.my_canvas.create_text(620,20,text="PHOTO",font="Times")
        self.my_canvas.create_line(0,40,720,40,fill="coral4")
        self.my_canvas.create_image(635,150,image=self.img)
        self.my_canvas.create_image(635,390,image=self.img1)

        self.my_canvas.create_text(63,150,text="Messi",font="Times")
        self.my_canvas.create_text(165,150,text="37",font="Times")
        self.my_canvas.create_text(250,150,text="Male",font="Times")
        self.my_canvas.create_text(350,150,text="Argentina",font="Times")
        self.my_canvas.create_text(470,150,text="ABC",font="Times")


        self.my_canvas.create_text(63,400,text="Ronaldo",font="Times")
        self.my_canvas.create_text(165,400,text="35",font="Times")
        self.my_canvas.create_text(250,400,text="Male",font="Times")
        self.my_canvas.create_text(350,400,text="Portugal",font="Times")
        self.my_canvas.create_text(470,400,text="XYZ",font="Times")



