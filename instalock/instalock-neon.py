import pyautogui
import time

time_limite = 10
time_inicial = time.time()
while True:
    pyautogui.click(958,916)
    sleep=0.3
    pyautogui.click(960,727)
    sleep=0.3
    time_atual = time.time()
    if time_atual - time_inicial >= time_limite:
        break
