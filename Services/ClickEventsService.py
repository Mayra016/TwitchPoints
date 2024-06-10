import pyautogui as py
import random

class ClickEventsService():

    def __init__(self, command) -> None:
        
        if 'random' in command.lower():
            self.randomPositionClick

        if 'click' in command.lower():
            self.click()

    def randomPositionClick():
        py.click(x=random.randrange(0, 1920), y=random.randrange(0, 1080)) 

    def click():
        py.click()    

