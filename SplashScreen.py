from tkinter import *
from PIL import ImageTk, Image, ImageFilter

class splashScreenFrames:
    def __init__(self, master):
        self.splash = Frame(master)

        # creating background image
        img_raw = Image.open('Images\SplashScreen.jpeg')
        raw_logo = Image.open('Images\DBMS_LOGO.png')
        raw_logo = raw_logo.resize((300, 300), Image.ANTIALIAS)
        img_raw = img_raw.resize((master.winfo_screenwidth(), master.winfo_screenheight()), Image.ANTIALIAS)
        img_raw = img_raw.filter(ImageFilter.GaussianBlur(3))
        img_raw.paste(raw_logo, ((master.winfo_screenwidth() // 3) + 120, 300), raw_logo)
        # done creating background image
        self.img = ImageTk.PhotoImage(img_raw)
        panel = Label(self.splash, image=self.img)
        panel.pack()
        self.splash.pack()


    def destroy_frame(self):
        self.splash.destroy()
