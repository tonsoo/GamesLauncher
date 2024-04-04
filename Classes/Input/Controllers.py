from pynput import keyboard

class KeyboardListener:

    pressed = {}

    def __init__(self) -> None:
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            self.pressed.__setitem__(key.char, True)
        except:
            self.pressed.__setitem__(f"{key}", True)

    def on_release(self, key):
        try:
            self.pressed.__setitem__(key.char, False)
        except:
            self.pressed.__setitem__(f"{key}", False)
    
    def isPressed(self, key:str) -> bool:
        return self.pressed.get(key)