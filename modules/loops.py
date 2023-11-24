from modules import frlg_pathing
from modules import ingame_controls as igc
from modules import automation as auto

def frlg_ip_exp_grind_loop(user_move, window_x, window_y):
    """
    Loop for FR/LG Indigo Plateau EXP grinding spot.
    """
    
    frlg_pathing.heal_pokemon_ip()
    print("Pokemon healed!")
    frlg_pathing.ip_to_vr()

    pp_ok = True
    while pp_ok:
        igc.fast_forward_start()
        igc.run_left_right()
        battle_state = auto.battle_check(window_x, window_y)
        if battle_state:
            igc.fast_forward_end()
            auto.battle(user_move, window_x, window_y)