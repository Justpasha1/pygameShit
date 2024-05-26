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
        self.Path = path
        self.Image = image.load(os.path.join(constans.path_to_folder, path))
        self.Image = transform.scale(self.Image, (width, height))
    def show(self, screen:display):
        screen.blit(self.Image, (self.X, self.Y))
class Creatures:
    def __init__(self, hp:int, dmg:int, df:int, gold:int, portrait:Image):
        self.HitPoints=hp
        self.CurHP = self.HitPoints
        self.Damage=dmg
        self.Defense=df
        self.CurDefense = 0
        self.Gold=gold
        self.CritChance = 25
        self.Portrait = portrait
        self.Portrait.__init__(portrait.Width,portrait.Height, portrait.Path, portrait.X, portrait.Y)
    def defence(self):
        self.CurDefense+=self.Defense
    def attacked(self, damage):
        if damage>self.CurDefense:
            self.CurHP-=damage-self.CurDefense
        else:
            return 0
class Text:
    def __init__(self, x:int, y:int , size:int, Font:str, text:str, color:tuple): 
        self.X=x
        self.Y=y
        self.Size=size
        self.Font=Font
        self.Text=text
        self.Color=color
        self.Font = font.SysFont(self.Font,self.Size)
        self.Text = self.Font.render(str(self.Text),False,self.Color)
    def ShowText(self,screen):
        screen.blit(self.Text, (self.X, self.Y))