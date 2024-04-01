import Definitions.Settings as conf
import tkinter as tk
import sys
import threading

class PageController(threading.Thread):

    WIDTH = 640
    HEIGHT = 480

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    
    def run(self):
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

        self.changePage('Home')

        self.mainWindow.mainloop()
    
    def callback(self) -> None:
        self.mainWindow.quit()
    
    def changePage(self, page: str) -> None:
        for widget in self.mainWindow.winfo_children():
            widget.destroy()

        self.currentPageName = page
        self.renderPage()

    def renderPage(self) -> None:
        currentPage = conf.DynamicImport("Classes.Generics.Pages", self.currentPageName)

        if(currentPage == None):
            if(self.currentPageName == 'Home'):
                print("Could not render any screens", file=sys.stderr)
                sys.exit()
            
            self.changePage('Home')
            return
        
        self.currentPage = currentPage(self)

        self.currentPage.renderPage(self.mainWindow)
