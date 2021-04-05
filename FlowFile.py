from tkinter import *
from SplashScreen import splashScreenFrames
from LoginScreen import loginScreenFrame
import time

splash = Tk()
width = splash.winfo_screenwidth()
height = splash.winfo_screenheight()
splash.state("zoomed")
splash.overrideredirect(True)
splashscreen = splashScreenFrames(splash)
splash.after(2000, lambda: splash.destroy())
splash.mainloop()



root = Tk()
root.title("FOOTBALL LEAGUE")
root.state("zoomed")
loginscreen = loginScreenFrame(root)
root.mainloop()


#screen = LoginScreen(root)

#logo = ImageTk.PhotoImage(raw_logo)
#canvas = Canvas(splash, width = 200, height = 300)
#canvas.create_image(0, 0, anchor=NW, image=logo)
#canvas.pack(pady=300)