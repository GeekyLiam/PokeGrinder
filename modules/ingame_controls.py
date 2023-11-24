import time
import keyboard

# Standard controls:

def up():
    time.sleep(0.4)
    keyboard.press("up")
    time.sleep(0.1)
    keyboard.release("up")

def down():
    time.sleep(0.4)
    keyboard.press("down")
    time.sleep(0.1)
    keyboard.release("down")

def left():
    time.sleep(0.4)
    keyboard.press("left")
    time.sleep(0.1)
    keyboard.release("left")

def right():
    time.sleep(0.4)
    keyboard.press("right")
    time.sleep(0.1)
    keyboard.release("right")

def a():
    time.sleep(0.4)
    keyboard.press("x")
    time.sleep(0.1)
    keyboard.release("x")

def b():
    time.sleep(0.4)
    keyboard.press("z")
    time.sleep(0.1)
    keyboard.release("z")

def start():
    time.sleep(0.4)
    keyboard.press("enter")
    time.sleep(0.1)
    keyboard.release("enter")

def select():
    time.sleep(0.4)
    keyboard.press("backspace")
    time.sleep(0.1)
    keyboard.release("backspace")

def l_bumper():
    time.sleep(0.4)
    keyboard.press("a")
    time.sleep(0.1)
    keyboard.release("a")

def r_bumper():
    time.sleep(0.4)
    keyboard.press("s")
    time.sleep(0.1)
    keyboard.release("s")

# Other:

def fast_forward_start():
    keyboard.press("tab")

def fast_forward_end():
    keyboard.release("tab")

def run_start():
    keyboard.press("z")

def run_end():
    keyboard.release("z")

def run_left_right():

    # Timed with fast_forward in mind:

    keyboard.press("left")
    time.sleep(0.2)
    keyboard.release("left")
    keyboard.press("right")
    time.sleep(0.2)
    keyboard.release("right")
