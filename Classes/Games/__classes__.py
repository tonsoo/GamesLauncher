from Classes.Input.Controllers import KeyboardListener

class Game:

    def __init__(self, gameName:str, gameImage:str, inputListener:KeyboardListener) -> None:
        self.name = gameName
        self.image = gameImage
        self.input = inputListener

        self.start()
    
    def start(self):
        pass

    def update(self):
        pass
    
    def pause(self):
        pass