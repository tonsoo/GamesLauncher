from Classes.Generics.PageController import PageController
from Classes.Input.Controllers import KeyboardListener

class App:

    def __init__(self):
        self.inputController = KeyboardListener()
        self.controller = PageController(self.inputController)