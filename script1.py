import pyautogui
import time
import win32api

time.sleep(1)
print("Starting...")

while True:
    for x in range(1,12):
        try:
            img = pyautogui.locateCenterOnScreen(f"{x}.PNG", confidence=0.35, region=(350,100,1300,700))
            win32api.SetCursorPos((img[0],img[1]))
            print("Monster found.")
            time.sleep(0.1)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(0.5)
        except:
            print("No monster found.")
    pyautogui.moveTo(1000, 450)
    pyautogui.dragTo(600, 450, 1, button='right')
    pyautogui.press('f5')
    print("End of the loop. Repeating...")
