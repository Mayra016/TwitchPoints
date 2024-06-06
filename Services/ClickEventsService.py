import pyautogui as py
import random

class ClickEventsService():

    def randomPositionClick():
        py.click(x=random.randrange(0, 1920), y=random.randrange(0, 1080)) 

    def click():
        py.click()    

