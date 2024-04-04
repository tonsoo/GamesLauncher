import tkinter as tk
from Classes.Generics.Page import Page
from Classes.Generics.PageController import PageController

class Home(Page):

    def __init__(self, pageController:PageController) -> None:
        Page.__init__(self, pageController=pageController, pageName="Home", pageTitle='Home', pageIcon='sid-el-cienceiro.ico')
    
    def renderItems(self, window:tk.Tk) -> None:
        myButton = tk.Button(window, bg='#342266', text="next", command=lambda: self.controller.changePage('Teste'))
        myButton.grid(row=0, column=13)

        myButton.pack()

        self.teste = tk.Label(window, text="Teste aaa", fg="#000")
        self.teste.pack()

        self.x = 0
        self.y = 0

    def update(self):
        if(self.controller.inputController.isPressed('a')):
            print('Pressionando o "a"')

        if(self.controller.inputController.isPressed('d')):
            print('OMAGAAH')

        self.teste.place(x=self.x, y=self.y)

        if(self.keyDown('Key.right')):
            self.x = self.x + 1
        elif(self.keyDown('Key.left')):
            self.x = self.x - 1
        
        if(self.keyDown('Key.up')):
            self.y = self.y - 1
        elif(self.keyDown('Key.down')):
            self.y = self.y + 1