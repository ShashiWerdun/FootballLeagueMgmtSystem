from tkinter import *
from PIL import ImageTk, Image, ImageFilter

splash = Tk()
width = splash.winfo_screenwidth()
height = splash.winfo_screenheight()
splash.state("zoomed")
splash.title("Splash Screen")
splash.overrideredirect(True)

img_raw = Image.open('Images\SplashScreen.jpeg')
raw_logo = Image.open('Images\DBMS_LOGO.png')
raw_logo = raw_logo.resize((300,300), Image.ANTIALIAS)
img_raw = img_raw.resize((width, height), Image.ANTIALIAS)
img_raw = img_raw.filter(ImageFilter.GaussianBlur(3))
img_raw.paste(raw_logo, ((width//3)+120, 300), raw_logo)
img = ImageTk.PhotoImage(img_raw)
panel = Label(splash, image=img)
panel.place(x=0, y=0, relwidth=1, relheight=1)



#logo = ImageTk.PhotoImage(raw_logo)
#canvas = Canvas(splash, width = 200, height = 300)
#canvas.create_image(0, 0, anchor=NW, image=logo)
#canvas.pack(pady=300)

def nextPage():
    splash.destroy()
    pass

splash.after(3000, nextPage)

mainloop()
