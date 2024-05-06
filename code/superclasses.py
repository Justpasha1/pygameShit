from pygame import *
import os, constans
init()

class Image:
    def __init__(self, width:int, height:int, path:str, x:int, y:int) -> None:
        '''
        This class is for showing images on the screen
            Parameters:
                :param width - the width of the image
                :param height - the height of the image
                :param path - path from the folder with game to file
                :param x - x position of image on screen
                :param y - y position of image on screen (inverted)
        '''
        self.Width = width
        self.Height = height
        self.X = x
        self.Y = y
        self.Image = image.load(os.path.join(constans.path_to_folder, path))
        self.Image = transform.scale(self.Image, (width, height))
    def show(self, screen:display):
        screen.blit(self.Image, (self.X, self.Y))