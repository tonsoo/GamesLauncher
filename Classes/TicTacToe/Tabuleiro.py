from random import randrange

class Tabuleiro:

    def __init__(self):
        self.width = 3
        self.height = 3

        self.players = 2
        self.turn = randrange(1, self.players + 1)

        print(f"width: {self.width}\nheight: {self.height}\nplayers: {self.players}\nturn: {self.turn}")
    
    def render(self):
        print("Rendering")
    