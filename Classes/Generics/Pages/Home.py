import tkinter as tk
from Classes.Generics.Page import Page
from Classes.Generics.PageController import PageController

class Home(Page):

    def __init__(self, pageController:PageController) -> None:
        Page.__init__(self, pageController=pageController, pageName="Home", pageTitle='Home', pageIcon='sid-el-cienceiro.ico')
    
    def renderItems(self, window:tk.Tk) -> None:
        myButton = tk.Button(window, bg='#342266', text="next", command=lambda: self.controller.changePage('Teste'))
        myButton.grid(row=0, column=13)

    def update(self):
        if(self.controller.inputController.isPressed('a')):
            print('Pressionando o "a"')