from tkinter import *
from PIL import ImageTk, Image
from Classes.Generics.Page import Page
from Classes.Generics.PageController import PageController
import Definitions.Settings as conf

class Home(Page):

    def __init__(self, pageController:PageController) -> None:
        Page.__init__(self, pageController=pageController, pageName="Home", pageTitle='Home', pageIcon='sid-el-cienceiro.ico')
    
    def renderItems(self, window:Tk) -> None:
        window.configure(background='#f00')
        self.panel = Label(window, image=conf.LoadImage(path='icons/aaa.png', x=27, y=27), background='#080', compound='left')

    def update(self):
        self.panel.place(x=self.x, y=self.y)
        print(f"Object placed at {self.x}x{self.y}")
        if(self.keyDown('Key.right')):
            self.x = self.x + 1
        elif(self.keyDown('Key.left')):
            self.x = self.x - 1
        
        if(self.keyDown('Key.up')):
            self.y = self.y - 1
        elif(self.keyDown('Key.down')):
            self.y = self.y + 1