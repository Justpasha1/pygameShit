from pygame import *
import os, constans, superclasses, buttons, images, global_vars
from random import randint
init()
#screen init##########################
screen = display.set_mode((800, 600))
display.set_caption("RPG")
display.set_icon(image.load(os.path.join(constans.path_to_folder,"images\\icons\\icon.png")))
# display.
screen.fill((randint(0,255),randint(0,255),randint(0,255)))

def hello():
    print("Hello world")

test = buttons.Buttons(41*4, 19*4, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"], 100, 100, hello)
######################################
def game():
    while True:
        images.base_ui.show(screen)
        global_vars.plr.Portrait.show(screen)
        for i in event.get():
            if i.type == QUIT:
                return False
            elif i.type == MOUSEBUTTONDOWN:
                test.click(mouse.get_pos())
            elif i.type == MOUSEMOTION:
                test.hover(mouse.get_pos())
        display.flip()
game()
