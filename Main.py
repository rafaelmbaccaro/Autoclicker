import threading
import time
import keyboard
import pyautogui as py

clicando = False
executando = True

def loop_cliques():
  while executando:
    if clicando:
      py.click()
    else:
      
      time.sleep(0.01)

t = threading.Thread(target=loop_cliques, daemon=True)
t.start()

while executando:
  if keyboard.is_pressed("p"):
    executando = False
    clicando = False
    break

  if keyboard.is_pressed("t"):
    clicando = not clicando
    time.sleep(0.2)

  if not clicando:
    time.sleep(0.05)