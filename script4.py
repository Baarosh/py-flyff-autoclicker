import pyautogui
import time
import win32api

leftbottom_x = 560
leftbottom_y = 600
rightbottom_x = 1250
rightbottom_y = 600
lefttop_x = 560
lefttop_y = 250
righttop_x = 1250
righttop_y = 250
jump = 150
width = 99
height = 99
flag = False
starttime = 5

time.sleep(2)
print("Starting...")

while True:
    try:
        img = pyautogui.locateAllOnScreen('Name.png', region=(500,200,700,450), confidence=0.80)
        if (img != None):
            print("I see it ", img)
            # win32api.SetCursorPos((img[0],img[1]+30))
            # time.sleep(0.05)
            # pyautogui.click(clicks=2, interval=0.15)
            # flag = True
            time.sleep(1)
            # starttime = 0
        else:
            print("I dont see it")
            # win32api.SetCursorPos((1000,400))
            # time.sleep(0.2)
            # if(flag == True):
            #     starttime = time.time()
            # if(time.time() - starttime > 2):
            #     pyautogui.moveTo(1000, 450)
            #     pyautogui.dragTo(600, 450, 0.5, button='right')
            #     pyautogui.press('f5')
            stime.sleep(1)
            # flag = False
    except:
        print("Error")
        time.sleep(0.5)
    # for y in range(leftbottom_y,lefttop_y, -jump):
    #     for x in range(leftbottom_x, rightbottom_x, jump):
    #         screenshot = pyautogui.screenshot('test.png', region=(x,y,width,height))
    #         width, height = screenshot.size

    #         for pix_x in range(0,99,25):
    #             for pix_y in range(0,99,25):
    #                 try:
    #                     win32api.SetCursorPos((x+pix_x,y+pix_y))
    #                     # r,g,b = screenshot.getpixel((pix_x,pix_y))
    #                     # if r<= 70 and g <= 40:
    #                     if (pyautogui.pixelMatchesColor(x+pix_x, y+pix_y, (70, 20, 10), tolerance=10)):
    #                         pyautogui.click(clicks=2, interval=0.2)
    #                         print("Monster found.")
    #                         time.sleep(3)
    #                     else:
    #                         print("Monster not found.")
    #                 except:
    #                     print("Error")
    # print("End of the loop. Repeating...")

    # pyautogui.moveTo(1000, 450)
    # pyautogui.dragTo(600, 450, 1, button='right')
    # pyautogui.press('f5')
