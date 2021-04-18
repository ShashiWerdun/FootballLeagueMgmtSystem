from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from ScreenTemplate import template


class favouritesScreenframe(template):
    def __init__(self, master):
        super().__init__(master)
        self.favscreenframe = Frame(self.baseFrame)
        self.favscreenframe.place(x=0, y=50, relwidth=1, relheight=1)
        Label(self.favscreenframe, text="Your Favourites", font=("Constantia", 20, "bold")).pack()
        Label(self.favscreenframe, text="Your Favourite Players", font=("Constantia", 16, "bold")).place(x=7, y=60)
        self.favplayer_main_frame = Frame(self.favscreenframe)
        self.favplayer_main_frame.place(x=7, y=90, relwidth=0.97, relheight=0.2)
        self.favplayer_canvas = Canvas(self.favplayer_main_frame)
        self.favplayer_canvas.place(x=0, y=0, relwidth=1)
        self.favplayer_scroll_bar = ttk.Scrollbar(self.favscreenframe, orient=HORIZONTAL,
                                                  command=self.favplayer_canvas.xview)
        self.favplayer_scroll_bar.place(anchor=SW, x=0, y=280, relwidth=1)
        self.favplayer_canvas.configure(xscrollcommand=self.favplayer_scroll_bar.set)
        self.favplayer_canvas.bind('<Configure>',
                                   lambda e: self.favplayer_canvas.configure(
                                       scrollregion=self.favplayer_canvas.bbox("all")))
        self.favplayer_Frame = Frame(self.favplayer_canvas)
        self.favplayer_canvas.create_window((0, 0), window=self.favplayer_Frame, anchor="nw")
        self.imageimage = ImageTk.PhotoImage(Image.open("Images\messi.png").resize((100, 100), Image.ANTIALIAS))
        for option in range(25):
            self.sty = ttk.Style()
            self.sty.configure("fvpl.TButton", font=("Comic Sans MS", 8, "bold"))
            ttk.Button(self.favplayer_Frame,
                   text="Messi\nage:35\nThoop Player",
                       image=self.imageimage,
                   style = "fvpl.TButton",
                   compound=TOP).pack(side=LEFT, padx=5)
        # favplayers done

        Label(self.favscreenframe, text="Your Favourite Managers", font=("Constantia", 16, "bold")).place(x=7, y=310)
        self.favmanager_main_frame = Frame(self.favscreenframe)
        self.favmanager_main_frame.place(x=7, y=340, relwidth=0.97, relheight=0.2)
        self.favmanager_canvas = Canvas(self.favmanager_main_frame)
        self.favmanager_canvas.place(x=0, y=0, relwidth=1)
        self.favmanager_scroll_bar = ttk.Scrollbar(self.favscreenframe, orient=HORIZONTAL,
                                                  command=self.favmanager_canvas.xview)
        self.favmanager_scroll_bar.place(anchor=SW, x=0, y=530, relwidth=1)
        self.favmanager_canvas.configure(xscrollcommand=self.favmanager_scroll_bar.set)
        self.favmanager_canvas.bind('<Configure>',
                                   lambda e: self.favmanager_canvas.configure(
                                       scrollregion=self.favmanager_canvas.bbox("all")))
        self.favmanager_Frame = Frame(self.favmanager_canvas)
        self.favmanager_canvas.create_window((0, 0), window=self.favmanager_Frame, anchor="nw")
        self.manaimage = ImageTk.PhotoImage(Image.open("Images\messi.png").resize((100, 100), Image.ANTIALIAS))
        for option in range(25):
            self.sty = ttk.Style()
            self.sty.configure("fvpl.TButton", font=("Comic Sans MS", 8, "bold"))
            ttk.Button(self.favmanager_Frame,
                       text="Messi\nage:35\nThoop Player",
                       image=self.manaimage,
                       style="fvpl.TButton",
                       compound=TOP).pack(side=LEFT, padx=5)
    # fav managers done
        Label(self.favscreenframe, text="Your Favourite Teams", font=("Constantia", 16, "bold")).place(x=7, y=560)
        self.favteam_main_frame = Frame(self.favscreenframe)
        self.favteam_main_frame.place(x=7, y=590, relwidth=0.97, relheight=0.2)
        self.favteam_canvas = Canvas(self.favteam_main_frame)
        self.favteam_canvas.place(x=0, y=0, relwidth=1)
        self.favteam_scroll_bar = ttk.Scrollbar(self.favscreenframe, orient=HORIZONTAL,
                                                   command=self.favteam_canvas.xview)
        self.favteam_scroll_bar.place(anchor=SW, x=0, y=780, relwidth=1)
        self.favteam_canvas.configure(xscrollcommand=self.favteam_scroll_bar.set)
        self.favteam_canvas.bind('<Configure>',
                                    lambda e: self.favteam_canvas.configure(
                                        scrollregion=self.favteam_canvas.bbox("all")))
        self.favteam_Frame = Frame(self.favteam_canvas)
        self.favteam_canvas.create_window((0, 0), window=self.favteam_Frame, anchor="nw")
        self.teamimage = ImageTk.PhotoImage(Image.open("Images\messi.png").resize((100, 100), Image.ANTIALIAS))
        for option in range(25):
            self.sty = ttk.Style()
            self.sty.configure("fvpl.TButton", font=("Comic Sans MS", 8, "bold"))
            ttk.Button(self.favteam_Frame,
                       text="Messi\nage:35\nThoop Player",
                       image=self.teamimage,
                       style="fvpl.TButton",
                       compound=TOP).pack(side=LEFT, padx=5)