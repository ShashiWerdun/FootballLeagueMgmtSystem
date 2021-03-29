from tkinter import *
from PIL import ImageTk, Image, ImageFilter

splash = Tk()
width = splash.winfo_screenwidth()
height = splash.winfo_screenheight()
splash.state("zoomed")
splash.title("Splash Screen")

img_raw = Image.open('Images\SplashScreen.jpeg')
img_raw = img_raw.resize((width, height), Image.ANTIALIAS)
img_raw = img_raw.filter(ImageFilter.GaussianBlur(3))
img = ImageTk.PhotoImage(img_raw)


panel = Label(splash, image=img)
panel.pack(side="bottom", fill="both",
           expand="yes")

def nextPage():
    panel.forget()
    pass

splash.after(2000, nextPage)

mainloop()
