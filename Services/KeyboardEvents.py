import pyautogui as py
import time

class KeyboardEventsService():

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
