import ctypes
import time
import win32gui
import keyboard
import getpixelcolor
import os

from modules import frlg_pathing
from modules import ingame_controls as igc

def frlg_ip_exp_grind_loop(user_move, window_x, window_y):
    
    frlg_pathing.heal_pokemon_ip()
    print("Pokemon healed!")
    frlg_pathing.ip_to_vr()

    pp_ok = True
    while pp_ok:
        igc.fast_forward_start()
        igc.run_left_right()
        battle_state = battle_check(window_x, window_y)
        if battle_state:
            igc.fast_forward_end()
            battle(user_move, window_x, window_y)

def menu_select(menu_option, window_x, window_y):
    """
    Opens menu in game, and selects given menu option by checking pixel colors.

    Param:
        menu_option: Menu option that needs to be selected
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window
    """

def battle(user_move, window_x, window_y):
    
    print("Battle started!")

    time.sleep(1)
    igc.a()
    time.sleep(2.5)

    battle_state = True

    while battle_state:
            battle_menu_select("fight", window_x, window_y)
            move_success = battle_move_menu_select(user_move, window_x, window_y)
            battle = battle_check(window_x, window_y)
            if not battle:
                print("Battle ended!")
                battle_state = False

def battle_check(window_x, window_y):
    """
    Checks if game is in battle state by checking pixel colors.

    Param:
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window

    Returns:
        If battle detected: True
        If battle not detected: False
    """

    pixel_color = getpixelcolor.pixel(window_x + 145, window_y + 160)
    if pixel_color == (255, 181, 66):
        return True
    else:
        return False
    
def pp_empty_check(window_x, window_y):
    """
    Checks if PP for selected move is empty by checking pixel colors.

    Param:
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window

    Returns:
        If PP empty: True
        If PP not empty: False
    """

    pixel_color = getpixelcolor.pixel(window_x + 514, window_y + 433)
    if pixel_color == (239, 0, 0):
        return True
    else:
        return False

def hp_low_check():

    # TODO: Implement function!!

    return False

def run_away():

    run_success = False
    while not run_success:

        igc.b()
        igc.right()
        igc.down()
        igc.a()
        time.sleep(1.5)

        check = run_check()
        if run_check:
            igc.a()
            return True
        else:
            igc.a()
            time.sleep(10)

def run_check(window_x, window_y):
    """
    Checks if running away was successful by checking pixel colors.

    Param:
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window

    Returns:
        If run attempt successful: True
        If run attempt not successful: False
    """

    pixel_color = getpixelcolor.pixel(window_x + 328, window_y + 435)
    if pixel_color == (255, 0, 0):
        return True
    else:
        return False
    
def battle_menu_select(menu_option, window_x, window_y):
    """
    Selects battle menu option.

    Param:
        menu_option: Menu option that needs to be selected
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window
    """

    in_menu = True

    while in_menu:
        if menu_option == "fight":
            igc.up()
            igc.left()
            pixel_color = getpixelcolor.pixel(window_x + 401, window_y + 437)
            if pixel_color == (41, 49, 49):
                igc.a()
                in_menu = False
        elif menu_option == "bag":
            igc.up()
            igc.right()
            pixel_color = getpixelcolor.pixel(window_x + 569, window_y + 437)
            if pixel_color == (41, 49, 49):
                igc.a()
                in_menu = False
        elif menu_option == "pokemon":
            igc.down()
            igc.left()
            pixel_color = getpixelcolor.pixel(window_x + 401, window_y + 486)
            if pixel_color == (41, 49, 49):
                igc.a()
                in_menu = False
        elif menu_option == "run":
            igc.down()
            igc.right()
            pixel_color = getpixelcolor.pixel(window_x + 569, window_y + 486)
            if pixel_color == (41, 49, 49):
                igc.a()
                in_menu = False

def battle_move_menu_select(user_move, window_x, window_y):
    """
    Selects battle menu option.

    Param:
        user_move: Move option that needs to be selected
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window

    Returns:
        If move has PP and is selected: True
        If move doesn't have PP and run away is initiated: False
    """

    in_move_menu = True

    while in_move_menu:
        if user_move == 1:
            igc.up()
            igc.left()
            pixel_color = getpixelcolor.pixel(window_x + 41, window_y + 436)
            if pixel_color == (41, 49, 49):
                pp_empty = pp_empty_check(window_x, window_y)
                if pp_empty:
                    run_status = run_away()
                    return False
                igc.a()
                time.sleep(10)
                igc.a()
                time.sleep(1.5)
                igc.a()
                in_move_menu = False
                return True

        if user_move == 2:
            igc.up()
            igc.right()
            pixel_color = getpixelcolor.pixel(window_x + 258, window_y + 436)
            if pixel_color == (41, 49, 49):
                pp_empty = pp_empty_check(window_x, window_y)
                if pp_empty:
                    run_status = run_away()
                    return False
                igc.a()
                time.sleep(10)
                igc.a()
                time.sleep(1.5)
                igc.a()
                in_move_menu = False
                return True

        if user_move == 3:
            igc.down()
            igc.left()
            pixel_color = getpixelcolor.pixel(window_x + 41, window_y + 486)
            if pixel_color == (41, 49, 49):
                pp_empty = pp_empty_check(window_x, window_y)
                if pp_empty:
                    run_status = run_away()
                    return False
                igc.a()
                time.sleep(10)
                igc.a()
                time.sleep(1.5)
                igc.a()
                in_move_menu = False
                return True

        if user_move == 4:
            igc.down()
            igc.right()
            pixel_color = getpixelcolor.pixel(window_x + 257, window_y + 486)
            if pixel_color == (41, 49, 49):
                pp_empty = pp_empty_check(window_x, window_y)
                if pp_empty:
                    run_status = run_away()
                    return False
                igc.a()
                time.sleep(10)
                igc.a()
                time.sleep(1.5)
                igc.a()
                in_move_menu = False
                return True

def user_move_select():
    """
    Allows user to select which move to spam against wild pokemon.
    """

    input_num_check = True
    while input_num_check:
        input_check = True
        while input_check:
            try:
                move_select = int(input("Enter number for move you wish to spam (1, 2, 3 or 4): \n"))
                input_check = False
            except:
                print("Invalid input. Try again: ")

        if move_select == 1:
            return 1
        elif move_select == 2:
            return 2
        elif move_select == 3:
            return 3
        elif move_select == 4:
            return 4
        else:
            print("Invalid input. Try again: ")

def get_fg_window_title():
    """
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
            user_move = user_move_select()
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


    # testing below

    frlg_ip_exp_grind_loop(user_move, window_x, window_y)

def main():

    menu()

if __name__ == "__main__":

    main()
