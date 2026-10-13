import pyautogui as py
import time
import keyboard
import pydirectinput as p
time.sleep(3)
while True:
    
    py.mouseDown(button='left')
    time.sleep(0.6)
    py.mouseUp(button='left')
    p.keyDown("enter")
    p.keyUp("enter")
    if keyboard.is_pressed('t'):
        break
