import Definitions.Settings as CONFIG
import tkinter as tk
import sys


class PageController:

    WIDTH = 640
    HEIGHT = 480

    def __init__(self, pageToRender:str):

        self.mainWindow = tk.Tk()

        self.mainWindow.configure(background="#ffffff")
        self.mainWindow.resizable(False, False)

        screen_width = self.mainWindow.winfo_screenwidth()
        screen_height = self.mainWindow.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.WIDTH/2))
        y_cordinate = int((screen_height/2) - (self.HEIGHT/2))

        self.mainWindow.minsize(self.WIDTH, self.HEIGHT)
        self.mainWindow.maxsize(self.WIDTH, self.HEIGHT)
        self.mainWindow.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x_cordinate}+{y_cordinate}")

        self.changePage(pageToRender)
    
    def changePage(self, page: str) -> None:
        self.currentPageName = page
        self.renderPage()

    def renderPage(self) -> None:
        # currentPage = conf.PAGES_DIR__dynamicImport("Classes.Generics.Pages", self.currentPageName)

        # if(currentPage == None and self.currentPageName == 'Home'):
        #     print("Could not render any screens", file=sys.stderr)
        #     sys.exit()
        
        # self.currentPage = currentPage

        # self.currentPage.renderPage(self.mainWindow)
        ...
