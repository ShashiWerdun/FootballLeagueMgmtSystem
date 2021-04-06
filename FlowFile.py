from tkinter import *
from SplashScreen import splashScreenFrames
from LoginScreen import loginScreenFrame
from reg_screen import Reg_screen
from HomePage import HomeScreenFrameGen
from ProfileScreen import ProfileScreen


def changeScreens(startscreen, endscreen):
    startscreen.destroy_frame()
    endscreen.start_frame()

def startup():
    global root
    root.overrideredirect(False)
    root.title("FOOTBALL LEAGUE")
    root.state("zoomed")
    root.resizable(0, 0)
    changeScreens(splash_screen, login_screen)


root = Tk()

# Preparing all Screens for use
splash_screen = splashScreenFrames(root)
login_screen = loginScreenFrame(root)
home_screen = HomeScreenFrameGen(root)
registration_screen = Reg_screen(root)
profile_screen = ProfileScreen(root)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.state("zoomed")
root.overrideredirect(True)
root.after(3000, lambda: startup())

login_screen.loginbutton.config(command=lambda: changeScreens(login_screen, home_screen))
login_screen.anonylogin.config(command=lambda: changeScreens(login_screen, home_screen))
login_screen.registerbutton.config(command=lambda: changeScreens(login_screen, registration_screen))

home_screen.profilebutton.config(command=lambda: changeScreens(home_screen, profile_screen))




root.mainloop()
