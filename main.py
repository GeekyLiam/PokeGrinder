import ctypes
import time
import win32gui
import keyboard
import getpixelcolor

from modules import frlg
from modules import ingame_controls as igc

def menu_select(menu_option):
    """
    Opens menu in game, and selects given menu option by checking pixel colors.
    Param: menu_option: Which menu option you want to select.
    """

    #TODO: make function adaptable to window position changes by +/- from x/y pos - make window pos modifiable within an ini file.

def battle():
    pass

def battle_check():
    """
    Checks if game is in battle state by checking pixel colors.
    Runs battle function if in battle, returns False if not in battle.
    """

    #TODO: make function adaptable to window position changes by +/- from x/y pos - make window pos modifiable within an ini file.

    pixel_color = getpixelcolor.pixel(195, 229)
    if pixel_color == (255, 181, 66):
        battle()
    else:
        return False
    
def hp_check():
    pass

def shiny_check():
    pass

def stuck():
    """
    Attempts to check if user is stuck, and attempts to correct to allow grinding to continue.
    """

    #TODO: 
    # Make modifiable within an ini file to allow user to choose whether to allow 
    # stuck() function to attempt to correct or to just quit upon stuck detection.

    # If no battle detected for ~1 min, attempt to unstuck...

    pass

def battle_menu_select():
    pass

def battle_move_menu_select():
    pass

def move_select():
    """
    Allows user to select which move to spam against wild pokemon.
    """
    #1,2,3,4...
    pass

def get_fg_window_title():
    """
    Returns title of currently active window.
    """

    hWnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hWnd)
    buf = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    if buf.value:
        return buf.value
    else:
        return None
    
def mgba_running_check():
    """
    Checks if mGBA is the active window.
    Returns True/False.
    """

    # Countdown to allow user time to select mGBA as active window.
    print("Starting countdown for active window check!")
    print("Make sure mGBA is your active window now!")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    title = get_fg_window_title()
    print(f"Current window: {title}")
    title_check = title.find("mGBA")
    if title_check == 0:
        print("mGBA detected! Starting poke-exp-bot...")
        mgba_win_handle = win32gui.FindWindow(None, get_fg_window_title())
        win32gui.MoveWindow(mgba_win_handle, 100, 100, 500, 400, 0) #TODO: Make x/y values modifiable within an ini file.
        time.sleep(1)
        return True
    else:
        print("Failed to detect mGBA as active window.\n")
        time.sleep(3)
        return False

def menu():
    """
    Menu function.
    """

    print("Welcome to poke-exp-bot! \nPlease ensure you have followed the instructions as stated in the README file.")
    start_loop = True
    while start_loop:
        start = input("Please enter s to start poke-exp-bot or q to quit. \n").upper()
        if start == "S":
            start_loop = False
            mgba_check_menu_loop = True
            while mgba_check_menu_loop:
                mgba_check = mgba_running_check()
                if mgba_check == True:
                    mgba_check_menu_loop = False
                else: 
                    mgba_check_menu_loop = True
        elif start == "Q":
            exit()
        elif start == "TEST": # Skips mGBA check sequence to allow for faster testing.
            time.sleep(2.5)
            start_loop = False
        else:
            print("Input not recognized.\n")

    #modules.frlg.fly_ip()

def main():

    #menu()
    time.sleep(2)
    igc.down()
    igc.up()
    igc.left()
    igc.right()

if __name__ == "__main__":

    main()