import pyautogui
import time
import win32api

time.sleep(2)
print("Starting...")

for x in range (0,10):
    pyautogui.screenshot(f"screenshot{x}.png", region=(320,90,1270,840))
    print(f"#{x} Screenshot made.")
    time.sleep(0.3)













# leftdown : 320, 930
# rightdown: 1590, 930
# lefttop: 320, 90
# righttop: 1590, 90