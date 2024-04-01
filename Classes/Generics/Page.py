import tkinter as tk
from Definitions import Settings as conf

class Page:

    pageTitle = ''

    def __init__(self, pageTitle:str = 'New Page', pageIcon:str = '') -> None:
        self.pageTitle = pageTitle
        self.pageIcon = pageIcon
    
    def renderPage(self, window:tk.Tk):
        window.title(self.pageTitle)
        
        pageIcon = conf.__buildPath(f"Files/{self.pageIcon}", start=conf.FILES_DIR)
        if conf.__isFile(pageIcon):
            window.iconbitmap(pageIcon)

        window.mainloop()