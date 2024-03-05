import pyautogui
import time

time_limite = 10
time_inicial = time.time()
while True:
    pyautogui.click(1218,921)
    sleep=0.2
    pyautogui.click(960,727)
    sleep=0.2
    time_atual = time.time()
    if time_atual - time_inicial >= time_limite:
        break
