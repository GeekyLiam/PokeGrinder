
def user_move_select():
    """
    Allows user to select which move to spam against wild pokemon.

    Returns:
        int value of selected move (1, 2, 3, 4)
    """

    # TODO: Allow user to select multiple moves to use 

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

def game_selection():
    # TODO: Implement game selection function (R/S/E, romhacks, etc.)
    pass

def location_selection():
    # TODO: Implement location selection to allow different grinding spots/loops
    pass

def mode_selection():
    # TODO: Implement mode selection (shiny hunting mode?)
    pass
