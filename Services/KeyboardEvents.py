import pyautogui as py
import time

class KeyboardEventsService():

    def __init__(self, command) -> None:
        if 'w' in command.lower():
            self.pressW

        if 'a' in command.lower():
            self.pressA

        if 's' in command.lower():
            self.pressS   

        if 'd' in command.lower():
            self.pressD

        if 'space' in command.lower():
            self.pressSpace

        if 'tab' in command.lower():
            self.pressTab    

        if 'hold' in command.lower():
            key = command.split(" ")
            self.holdKey(key[1])        

    def pressW(self):
        self.holdKey('w')

    def pressA(self):
        self.holdKey('a')  

    def pressS(self):
        self.holdKey('s')

    def pressD(self):
        self.holdKey('d')  

    def pressSpace(self):
        self.holdKey('space')

    def pressTab(self):
        self.holdKey('tab')    

    def holdKey(key):
        py.keyDown(key)  
        time.sleep(2)  
        py.keyUp(key)
