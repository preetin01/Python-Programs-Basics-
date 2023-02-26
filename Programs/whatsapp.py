import pyautogui as pg
import time
print("starting in 4 seconds...")
time.sleep(5)

for i in range(100):
    pg.write("Hello,deeksha")
    pg.press("enter")