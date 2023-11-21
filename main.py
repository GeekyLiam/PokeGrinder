import ctypes
import time

def get_fg_window_title():
    """
    Function to return title of currently active window.
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
    Function to check if mGBA is the active window.
    Returns True/False.
    """

    # Countdown to allow user time to select mGBA as active window
    print("Starting countdown for active window check!")
    print("Make sure mGBA is your active window now!")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    title = get_fg_window_title()
    print(f"Current window: {title}")
    title_check = title.find("mGBA")
    if title_check == 0:
        print("mGBA detected! Starting PokeGrinder...")
        time.sleep(1)
        return True
    else:
        print("Failed to detect mGBA as active window.\n")
        time.sleep(3)
        return False

def heal_pokemon_fr_ip():
    pass

def move_select():
    #1,2,3,4...
    pass

def menu():

    print("Welcome to PokeGrinder! \nPlease ensure you have followed the instructions as stated in the README file.")
    start_loop = True
    while start_loop:
        start = input("Please enter s to start PokeGrinder or q to quit. \n").upper()
        if start == "S":
            start_loop = False
        elif start == "Q":
            exit()
        else:
            print("Input not recognized.\n")

    mgba_check_menu_loop = True
    while mgba_check_menu_loop:
        mgba_check = mgba_running_check()
        if mgba_check == True:
            mgba_check_menu_loop = False
        else: 
            mgba_check_menu_loop = True

def main():
    menu()

if __name__ == "__main__":
    main()