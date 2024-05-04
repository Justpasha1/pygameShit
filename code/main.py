from pygame import *
import os, constans, superclasses
from random import randint
init()
#screen init##########################
screen = display.set_mode((800, 600))
display.set_caption("RPG")
display.set_icon(image.load(os.path.join(constans.path_to_folder,"images\\icons\\icon.png")))
# display.
screen.fill((randint(0,255),randint(0,255),randint(0,255)))

test = superclasses.Image(20, 20, "images\\icons\\icon.png", 100, 100)
######################################
def game():
    while True:
        test.show(screen)
        for i in event.get():
            if i.type == QUIT:
                print ('1')
                return False
        display.flip()
game()