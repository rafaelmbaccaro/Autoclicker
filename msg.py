import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ["teste de array!","Teste de array!"]

for i in range(15):
    time.sleep(1)
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")