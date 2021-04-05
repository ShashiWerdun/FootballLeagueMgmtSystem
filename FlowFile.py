from tkinter import *
from SplashScreen import splashScreenFrames
from LoginScreen import loginScreenFrame

def startup():
    global root
    global rootscreen
    root.overrideredirect(False)
    root.title("FOOTBALL LEAGUE")
    root.state("zoomed")
    rootscreen.forgetframe()
    loginScreenFrame(root)
    root.resizable(0, 0)


root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.state("zoomed")
root.overrideredirect(True)
rootscreen = splashScreenFrames(root)
root.after(3000, lambda: startup())
root.mainloop()

# root = Tk()
# root.title("FOOTBALL LEAGUE")
# root.state("zoomed")
# loginscreen = loginScreenFrame(root)
# root.resizable(0, 0)
# root.mainloop()
