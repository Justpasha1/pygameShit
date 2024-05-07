from pygame import *
import superclasses, constans, os

class Buttons(superclasses.Image):
    def __init__(self, width: int, height: int, paths: list, x: int, y: int, func: callable) -> None:
        self.Width = width
        self.Height = height
        self.X = x
        self.Y = y
        self.Images = []
        for i in paths:
            i = image.load(os.path.join(constans.path_to_folder, i))
            i = transform.scale(i, (width, height))
            self.Images.append(i)
        self.Image = self.Images[0]
        self.Func = func
    def click(self, coords):
        if (self.X<=coords[0]<= self.X+self.Width) and (self.Y<=coords[1] and self.Y+self.Height >= coords[1]):
            self.Func()
            self.Image = self.Images[2]
    def hover(self, coords):
        if (self.X<=coords[0]<= self.X+self.Width) and (self.Y<=coords[1] and self.Y+self.Height >= coords[1]):
            self.Image=self.Images[1]
        else:
            self.Image=self.Images[0]