import ctypes
import time
import win32gui
import keyboard
import getpixelcolor
import os

from modules import frlg_pathing
from modules import loops
from modules import menu_utils
from modules import automation as auto
from modules import ingame_controls as igc

def get_fg_window_title():
    """
    Finds title of currently active/focused window.

    Returns:
        Title of currently active window.
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

    Returns:
        If mGBA detected: tuple (True, window pos x, window pos y)
        If mGBA not detected: tuple (False, 0, 0)
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
        time.sleep(1.5)
        os.system("cls")
        mgba_win_handle = win32gui.FindWindow(None, get_fg_window_title())
        window_pos_info = win32gui.GetWindowRect(mgba_win_handle)
        time.sleep(1)
        return (True, window_pos_info[0], window_pos_info[1])
    else:
        print("Failed to detect mGBA as active window.\n")
        time.sleep(3)
        return (False, 0, 0)

def menu():
    """
    Menu function.

    Returns:
        tuple (user move, window pos x, window pos y)
    """

    print("Welcome to poke-exp-bot!")
    print("Please ensure you have followed the instructions as stated in the README file.")
    print("After poke-exp-bot has detected mGBA, do not move the mGBA window!")
    print("Do not obscure the mGBA window!")
    print("Ensure mGBA is set to 3x frame size in the Audio/Video drop down menu!")
    start_loop = True
    while start_loop:
        start = input("Please enter s to start poke-exp-bot or q to quit. \n").upper()
        if start == "S":
            user_move = menu_utils.user_move_select()
            start_loop = False
            mgba_check_menu_loop = True
            while mgba_check_menu_loop:
                mgba_info = mgba_running_check()
                window_x = mgba_info[1]
                window_y = mgba_info[2]
                if mgba_info[0] == True:
                    mgba_check_menu_loop = False
                else: 
                    mgba_check_menu_loop = True
        elif start == "Q":
            exit()
        elif start == "TEST": # Skips mGBA check sequence to allow for faster testing.
            start_loop = False
        else:
            print("Input not recognized. \n")

    return (user_move, window_x, window_y)

def main():

    data = menu()
    user_move = data[0]
    window_x = data[1]
    window_y = data[2]

    loops.frlg_ip_exp_grind_loop(user_move, window_x, window_y)

if __name__ == "__main__":

    main()
