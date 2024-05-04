from pygame import *
import os, constans
init()

class Image:
    def __init__(self, width:int, height:int, path:str, x:int, y:int) -> None:
        '''
        Parameters:
            width - the width of the image
            height - the height of the image
            path - path from the folder with game to file
            x - x position of image on screen
            width - y position of image on screen (inverted)
        '''
        self.Width = width
        self.Height = height
        self.X = x
        self.Y = y
        self.Image = image.load(os.path.join(constans.path_to_folder, path))
    def show(self, screen:display):
        screen.blit(self.Image, (self.X, self.Y))