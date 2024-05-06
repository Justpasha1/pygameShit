from pygame import *
import superclasses

class Buttons(superclasses.Image):
    def __init__(self, width: int, height: int, path: str, x: int, y: int, func: callable) -> None:
        super().__init__(width, height, path, x, y)
        self.Func = func
    def click(self, coords):
        if (self.X<=coords[0]<= self.X+self.Width) and (self.Y<=coords[1] and self.Y+self.Height >= coords[1]):
            self.Func()