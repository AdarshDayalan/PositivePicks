import pyautogui as pg
import time

pages = 4
sleepTime = 0.5

def scrapeFTN():
    for i in range(0, pages):
        pg.hotkey("alt", "tab")

        time.sleep(1)
        pg.click(400, 400)

        # time.sleep(1)
        # pg.scroll(-300)

        # time.sleep(1)
        # pg.click(x=730, y=300, button='right')
        # time.sleep(1)
        # pg.click(745, 910)

        # time.sleep(3)
        # pg.click(x=1560, y=260, button='right')
        # time.sleep(sleepTime)
        # pg.click(1585, 306)

        time.sleep(sleepTime)
        pg.hotkey("ctrlleft", "a")
        time.sleep(sleepTime)
        pg.hotkey("ctrlleft", "c")
        # time.sleep(sleepTime)
        # pg.click(1901, 134)

        time.sleep(sleepTime)
        pg.scroll(-1300)
        time.sleep(sleepTime)
        pg.click(1832, 374)
        time.sleep(sleepTime)
        pg.scroll(1300)

        time.sleep(sleepTime)
        pg.hotkey("alt", "tab")

        time.sleep(sleepTime)
        pg.click(222, 172)
        time.sleep(sleepTime)
        pg.click(222, 105)
        
        time.sleep(sleepTime)
        pg.typewrite("page"+str(i+1)+".txt")
        time.sleep(sleepTime)
        pg.typewrite(["enter"])

        time.sleep(sleepTime)
        pg.hotkey("ctrlleft", "v")
        time.sleep(sleepTime)
        pg.hotkey("ctrlleft", "s")
        time.sleep(sleepTime)
        pg.hotkey("ctrlleft", "w")