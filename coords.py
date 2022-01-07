import pyautogui
import time, random

while True:
    print(pyautogui.position())
    x = random.randint(151, 160)
    y = random.randint(199, 205)
    d = random.randint(1, 3)

    pyautogui.click(x, y, duration=d, tween=pyautogui.easeInOutSine)
    time.sleep(1)