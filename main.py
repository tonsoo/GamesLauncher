from Classes.Generics.PageController import PageController
from Classes.Input.Controllers import KeyboardListener

inputController = KeyboardListener()
controller = PageController(inputController)