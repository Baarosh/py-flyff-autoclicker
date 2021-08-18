import pyautogui
import time

while True:
    pyautogui.keyDown('f5')
    print('keydown...')
    time.sleep(0.5)
    pyautogui.keyUp('f5')
    print('key up')
    time.sleep(2)