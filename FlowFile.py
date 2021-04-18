from tkinter import *

from PIL import Image, ImageTk

from FavouritesScreen import favouritesScreenframe
from HomePage import HomeScreenFrameGen
from LoginScreen import loginScreenFrame
from ManagerList import managerlistFrame
from ManagerStatsScreen import ManagerStatsScreen
from MatchStatsScreen import MatchStatsScreen
from PlayerList import playerlistFrame
from PlayerStatsScreen import PlayerStatsScreen
from PointsTable import pointsTableFrame
from ProfileScreen import ProfileScreen
from SplashScreen import splashScreenFrames
from SponsorList import sponsorlistFrame
from TeamList import teamlistFrame
from TeamStatsScreen import TeamStatsScreen
from reg_screen import Reg_screen


def validationfunc(startscreen, endscreen):
    status = startscreen.validate()
    if status[0]:
        global userID
        userID = status[1]
        change_screens(startscreen, endscreen)


def stats_change(startscreen, endscreen, treeobject):
    focusid = treeobject.focus()
    primkey = (treeobject.item(focusid, 'values'))
    endscreen.__init__(root, primkey)
    change_screens(startscreen, endscreen)


def match_stats_change(startscreen, endscreen, treeobject):
    primkey = treeobject.focus()
    endscreen.__init__(root, primkey)
    change_screens(startscreen, endscreen)


def change_screens(startscreen, endscreen):
    startscreen.destroy_frame()
    global userID
    if endscreen == login_screen:
        userID = 0
    if userID == 0 and endscreen == home_screen:
        home_screen.profilebutton.place_forget()
    elif userID != 0 and endscreen == home_screen:
        home_screen.place_profile_button()
    global present_screen
    if endscreen is None:
        endscreen = screen_stack.pop()
    else:
        screen_stack.append(startscreen)
        endscreen.back_button.config(command=lambda: change_screens(present_screen, None))
    endscreen.start_frame()
    present_screen = endscreen


def startup():
    # starting the database
    # cx_Oracle.init_oracle_client(lib_dir=os.environ.get("TNS_ADMIN"))
    # screen change buttons
    login_screen.loginbutton.config(command=lambda: validationfunc(login_screen, home_screen))
    login_screen.anonylogin.config(command=lambda: change_screens(login_screen, home_screen))
    login_screen.registerbutton.config(command=lambda: change_screens(login_screen, registration_screen))

    registration_screen.loginredirect.config(command=lambda: change_screens(registration_screen, None))
    registration_screen.btn_register.config(command=lambda: validationfunc(registration_screen, login_screen))

    home_screen.profilebutton.config(command=lambda: change_screens(home_screen, profile_screen))
    home_screen.players_list_button.config(command=lambda: change_screens(home_screen, player_list_screen))
    home_screen.teams_list_button.config(command=lambda: change_screens(home_screen, team_list_screen))
    home_screen.managers_list_button.config(command=lambda: change_screens(home_screen, manager_list_screen))
    home_screen.logoutbutton.config(command=lambda: change_screens(home_screen, login_screen))
    home_screen.points_table_button.config(command=lambda: change_screens(home_screen, points_table_screen))
    home_screen.sponsors_list_button.config(command=lambda: change_screens(home_screen, sponsor_list_screen))

    profile_screen.favourites_button.config(command=lambda: change_screens(profile_screen, favourites_screen))
    team_list_screen.teams_tree.bind('<ButtonRelease-1>', lambda c: stats_change(team_list_screen, team_stat_screen,
                                                                                 team_list_screen.teams_tree))
    home_screen.matchschedule.bind('<ButtonRelease-1>',
                                   lambda c: match_stats_change(home_screen, match_stat_screen,
                                                                home_screen.matchschedule))
    player_list_screen.players_tree.bind('<ButtonRelease-1>',
                                         lambda c: stats_change(player_list_screen, player_stat_screen,
                                                                player_list_screen.players_tree))

    global root
    global image
    root.overrideredirect(False)
    root.title("FOOTBALLLAZA")
    root.iconphoto(False, image)
    root.state("zoomed")
    # root.resizable(0, 0)
    change_screens(splash_screen, login_screen)


root = Tk()

userID = 0

image = ImageTk.PhotoImage(Image.open("Images/DBMS_LOGO.png"))
screen_stack = []
present_screen = None

# Preparing all Screens for use
splash_screen = splashScreenFrames(root)
splash_screen.start_frame()
login_screen = loginScreenFrame(root)
home_screen = HomeScreenFrameGen(root)
registration_screen = Reg_screen(root)
profile_screen = ProfileScreen(root)
match_stat_screen = MatchStatsScreen(root)
player_list_screen = playerlistFrame(root)
player_stat_screen = PlayerStatsScreen(root)
points_table_screen = pointsTableFrame(root)
manager_list_screen = managerlistFrame(root)
manager_stat_screen = ManagerStatsScreen(root)
sponsor_list_screen = sponsorlistFrame(root)
team_list_screen = teamlistFrame(root)
team_stat_screen = TeamStatsScreen(root)
favourites_screen = favouritesScreenframe(root)

root.state("zoomed")
root.overrideredirect(True)
root.after(3000, lambda: startup())

root.mainloop()
