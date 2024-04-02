from Classes.Input.Controllers import KeyboardListener
from Classes.Games import __classes__ as classes

class TicTacToe(classes.Game):

    def __init__(self, gameName:str, gameImage:str, inputListener:KeyboardListener) -> None:
        classes.Game.__init__(self=self, gameName=gameName, gameImage=gameImage, inputListener=inputListener)
    
    def start(self):
        print('Starting a new game')

    def update(self):
        if(self.inputListener.isPressed('return')):
            print('Updating current game')
    
    def pause(self):
        pass