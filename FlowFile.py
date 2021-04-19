# import os
import socket
from tkinter import *
from tkinter import messagebox

import cx_Oracle
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


def row_open(treeobject):
    status = treeobject.item(treeobject.focus(), option='open')
    treeobject.item(treeobject.focus(), open=(not status))


def stats_change(startscreen, endscreen, treeobject):
    rowid = treeobject.parent(treeobject.focus())
    primkey = (treeobject.item(rowid, 'values'))
    endscreen.__init__(root, primkey)
    change_screens(startscreen, endscreen)


def add_to_fav(treeobject, table_name):
    if messagebox.askokcancel('Adding to favourites', 'Do you want to add this to favourites?'):
        rowid = treeobject.parent(treeobject.focus())
        primkey = (treeobject.item(rowid, 'values'))[0]
        connection = cx_Oracle.connect('project', 'oracle',
                                       dsn=cx_Oracle.makedsn(socket.gethostname(), '1521', service_name='XE'))
        try:
            connection.cursor().execute(f"insert into fav_{table_name} values({userID}, '{primkey}')")
            messagebox.showinfo('Added to favourites',
                                f'This {table_name} has been successfully added to your favourites list!')
        except cx_Oracle.IntegrityError:
            messagebox.showerror('Error adding to favourites', 'This item is already present in your favourites list!')
        connection.commit()
        connection.close()


def profile_button_click(startscreen, endscreen):
    endscreen.__init__(root, userID)
    favourites_screen.__init__(root, userID)
    endscreen.favourites_button.config(command=lambda: change_screens(profile_screen, favourites_screen))
    change_screens(startscreen, endscreen)


def match_stats_change():
    tree_object = home_screen.matchschedule
    match_stat_screen.__init__(root, tree_object.focus())
    change_screens(home_screen, match_stat_screen)


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

    home_screen.profilebutton.config(command=lambda: profile_button_click(home_screen, profile_screen))
    home_screen.players_list_button.config(command=lambda: change_screens(home_screen, player_list_screen))
    home_screen.teams_list_button.config(command=lambda: change_screens(home_screen, team_list_screen))
    home_screen.managers_list_button.config(command=lambda: change_screens(home_screen, manager_list_screen))
    home_screen.logoutbutton.config(command=lambda: change_screens(home_screen, login_screen))
    home_screen.points_table_button.config(command=lambda: change_screens(home_screen, points_table_screen))
    home_screen.sponsors_list_button.config(command=lambda: change_screens(home_screen, sponsor_list_screen))

    # TEAMS LIST BINDINGS
    # single click to show row options
    team_list_screen.teams_tree.bind('<ButtonRelease-1>', lambda c: row_open(team_list_screen.teams_tree))
    # click on open row to open team stats
    team_list_screen.teams_tree.tag_bind("open", sequence='<ButtonRelease-1>',
                                         callback=lambda e: stats_change(team_list_screen, team_stat_screen,
                                                                         team_list_screen.teams_tree))
    # click on add to favourites row to add to favourites
    team_list_screen.teams_tree.tag_bind("favourite", sequence='<ButtonRelease-1>',
                                         callback=lambda e: add_to_fav(team_list_screen.teams_tree, 'team'))

    # PLAYERS LIST BINDINGS
    # single click to show row options
    player_list_screen.players_tree.bind('<ButtonRelease-1>', lambda c: row_open(player_list_screen.players_tree))
    # click on open row to open team stats
    player_list_screen.players_tree.tag_bind("open", sequence='<ButtonRelease-1>',
                                             callback=lambda e: stats_change(player_list_screen, player_stat_screen,
                                                                             player_list_screen.players_tree))
    # click on add to favourites row to add to favourites
    player_list_screen.players_tree.tag_bind("favourite", sequence='<ButtonRelease-1>',
                                             callback=lambda e: add_to_fav(player_list_screen.players_tree, 'team'))

    # MANAGERS LIST BINDINGS
    # single click to show row options
    manager_list_screen.managers_tree.bind('<ButtonRelease-1>', lambda c: row_open(manager_list_screen.managers_tree))
    # click on open row to open team stats
    manager_list_screen.managers_tree.tag_bind("open", sequence='<ButtonRelease-1>',
                                               callback=lambda e: stats_change(manager_list_screen, manager_stat_screen,
                                                                               manager_stat_screen.managers_tree))
    # click on add to favourites row to add to favourites
    manager_list_screen.managers_tree.tag_bind("favourite", sequence='<ButtonRelease-1>',
                                               callback=lambda e: add_to_fav(manager_list_screen.managers_tree, 'team'))

    home_screen.matchschedule.bind('<ButtonRelease-1>', lambda c: match_stats_change())
    manager_list_screen.managers_tree.bind('<ButtonRelease-1>',
                                           lambda c: stats_change(manager_list_screen, manager_stat_screen,
                                                                  manager_list_screen.managers_tree))

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
