import tkinter as tk
from Definitions import Settings as conf
from Classes.Generics.PageController import PageController
import threading

class Page:

    pageTitle = ''

    def __init__(self, pageController:PageController, pageTitle:str = 'New Page', pageName:str = 'New Page', pageIcon:str = '') -> None:
        self.pageTitle = pageTitle
        self.pageIcon = pageIcon
        self.controller = pageController
        self.pageName = pageName

    def update(self):
        ...

    def keyDown(self, key:str) -> bool:
        return self.controller.inputController.isPressed(key)
    
    def keyUp(self, key:str) -> bool:
        return not self.controller.inputController.isPressed(key)

    def renderPage(self, window:tk.Tk):
        window.title(self.pageTitle)
        
        pageIcon = conf.BuildPath(f"Files/{self.pageIcon}", start=conf.FILES_DIR)
        if conf.IsFile(pageIcon):
            window.iconbitmap(pageIcon)
        
        self.renderItems(window)
        
    def renderItems(self, window:tk.Tk) -> None:
        window.mainloop()
    
    def changePage(self) -> None:
        self.controller.changePage(self.pageName)