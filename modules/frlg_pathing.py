import time
import keyboard

from modules import ingame_controls as igc

def heal_pokemon_ip():

    # Pathing from outside Indigo Plateau, inside to heal, and back outside again.

    igc.up()
    time.sleep(2.5)
    igc.up()
    igc.up()
    igc.up()
    igc.up()
    igc.right()
    igc.right()
    igc.right()
    igc.up()
    igc.a()
    time.sleep(1.5)
    igc.a()
    time.sleep(1.5)
    igc.a()
    time.sleep(8)
    igc.a()
    time.sleep(1.5)
    igc.a()
    igc.left()
    igc.left()
    igc.left()
    igc.down()
    igc.down()
    igc.down()
    igc.down()
    igc.down()
    igc.down()
    time.sleep(2.5)

def ip_to_vr():

    for i in range(15):
        igc.down()
    for i in range(5):
        igc.right()
    for i in range(10):
        igc.down()
    for i in range(2):
        igc.left()
    for i in range(8):
        igc.down()
    for i in range(8):
        igc.right()
    for i in range(12):
        igc.down()
    for i in range(4):
        igc.left()
    for i in range(2):
        igc.up()
    time.sleep(4)