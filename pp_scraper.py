import pyautogui as pg
import time
from utils import get_projection_names

names = get_projection_names()
print(names)

ySearch = 555
#605, 3. #555, 2
sleepTime = 0.5

for name in names:
    pg.hotkey("alt", "tab")
    
    time.sleep(sleepTime)
    pg.click(1070, ySearch) # Search
    time.sleep(sleepTime)
    pg.typewrite(name)
    
    time.sleep(sleepTime)
    pg.click(x=900, y=275, button='right') #Inspect
    time.sleep(sleepTime)
    pg.click(930, 830)

    time.sleep(3)
    pg.click(x=1515, y=430, button='right') #Edit HTML
    time.sleep(sleepTime)
    pg.click(1535, 480)

    time.sleep(sleepTime)
    pg.hotkey("ctrlleft", "a") #Copy HTML
    time.sleep(sleepTime)
    pg.hotkey("ctrlleft", "c")

    time.sleep(sleepTime)
    pg.click(1901, 134) #Close Inspect
    time.sleep(sleepTime)
    pg.scroll(500) #Scroll Up
    time.sleep(sleepTime)
    pg.click(1361, ySearch) #Clear Search

    time.sleep(sleepTime)
    pg.hotkey("alt", "tab")

    time.sleep(sleepTime)
    pg.click(222, 149)
    time.sleep(sleepTime)
    pg.click(222, 105)
    
    time.sleep(sleepTime)
    pg.typewrite(name+".txt")
    time.sleep(sleepTime)
    pg.typewrite(["enter"])

    time.sleep(sleepTime)
    pg.hotkey("ctrlleft", "v")
    time.sleep(sleepTime)
    pg.hotkey("ctrlleft", "s")
    time.sleep(sleepTime)
    pg.hotkey("ctrlleft", "w")