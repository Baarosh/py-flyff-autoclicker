import pyautogui
import time
import win32api
import datetime

FLAG = False
STARTTIME = time.time()
LEFT = 320
TOP = 30
WIDTH = 1590 - LEFT
HEIGHT = 985 - TOP
CENTER_X = int((LEFT + WIDTH) / 2)
CENTER_Y = int((TOP + HEIGHT) / 2)
RIGHT = LEFT + WIDTH
BOTTOM = TOP + HEIGHT

def Attack(img):
    global FLAG, STARTTIME
    print(f"Monster found at {img[0]}, {img[1]} ! ", datetime.datetime.now())
    win32api.SetCursorPos((img[0],img[1]+30))
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.05)
    pyautogui.keyDown('1')
    time.sleep(0.05)
    pyautogui.keyUp('1')
    win32api.SetCursorPos((CENTER_X, CENTER_Y))
    time.sleep(0.05)
    pyautogui.keyDown('s')
    time.sleep(0.05)
    pyautogui.keyUp('s')
    FLAG = True
    STARTTIME = 0

def Move():
    global FLAG, STARTTIME
    print("Monster not found! ", datetime.datetime.now())
    win32api.SetCursorPos((CENTER_X, CENTER_Y))
    time.sleep(0.05)
    if(FLAG == True):
        STARTTIME = time.time()
        FLAG = False
    if(time.time() - STARTTIME > 0.6):
        pyautogui.moveTo(CENTER_X + 300, CENTER_Y)
        pyautogui.dragTo(CENTER_X - 300, CENTER_Y, 0.2, button='right')
        FLAG = True

def RunScript():
    print("Starting...")
    time.sleep(2.0)
    print("Running...")

    while (win32api.GetCursorPos()[0] < RIGHT):
        try:
            first_img = pyautogui.locateCenterOnScreen('Meleth.png', region=(LEFT, TOP + 225, WIDTH , HEIGHT - 225), confidence=0.70)
            if (first_img == None):
                second_img = pyautogui.locateCenterOnScreen('Meleth.png', region=(LEFT, TOP, WIDTH , HEIGHT), confidence=0.70)
                if (second_img != None):
                    Attack(second_img)
                else:
                    Move()
                pyautogui.keyDown('f5')
                time.sleep(0.05)
                pyautogui.keyUp('f5')
            else:
                Attack(first_img)
        except:
            print("Error!")
            time.sleep(0.5)

RunScript()
