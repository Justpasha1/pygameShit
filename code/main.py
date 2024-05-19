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
        # test.show(screen)
        global_vars.button_attack.show(screen)
        global_vars.button_heal.show(screen)
        global_vars.button_deffence.show(screen)
        global_vars.heart_icon.show(screen)
        global_vars.shield_icon.show(screen)
        global_vars.sword_icon.show(screen)
        for i in event.get():
            if i.type == QUIT:
                return False
            elif i.type == MOUSEBUTTONDOWN:
                global_vars.button_attack.click(mouse.get_pos())
                # test.click(mouse.get_pos())
            elif i.type == MOUSEMOTION:
                pass
                # test.hover(mouse.get_pos())
        display.flip()
game()
