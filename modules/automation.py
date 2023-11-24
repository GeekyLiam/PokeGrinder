import time
import getpixelcolor

from modules import frlg_pathing
from modules import ingame_controls as igc

def menu_select(menu_option, window_x, window_y):
    """
    Opens menu in game, and selects given menu option by checking pixel colors.

    Param:
        menu_option: Menu option that needs to be selected
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window
    """

    # TODO: Needs to be implemented to allow flying

def battle(user_move, window_x, window_y):
    """
    Handles battles.

    Param:
        user_move: Move to be selected
        window_x: X postion of mGBA window
        window_y: Y position of mGBA window
    """
    
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
    """
    Attempts to run away from a wild battle.
    
    Returns:
        If run attempt successful: True
        If run attempt not successful: False
    """

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
        If run attempt check successful: True
        If run attempt check not successful: False
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
