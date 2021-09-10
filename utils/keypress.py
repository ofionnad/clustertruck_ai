from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import time 

time.sleep(2)

keyboard = Controller()
key = "a"

keyboard.press(key)
keyboard.release(key)