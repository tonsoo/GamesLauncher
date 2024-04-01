import tkinter as tk
from Classes.Generics.Page import Page
from Classes.Generics.PageController import PageController

class Teste(Page):

    def __init__(self, pageController:PageController) -> None:
        Page.__init__(self, pageController=pageController,pageName="Teste", pageTitle='Teste alaaa', pageIcon='sid-el-cienceiro.ico')
    
    def renderItems(self, window:tk.Tk) -> None:
        myButton = tk.Button(window, bg='#343434', text="next", command=lambda: self.controller.changePage('Home'))
        myButton.place(x=40, y=80)
        myButton.grid(row=10, column=13)