from buttons import *
from superclasses import *
import pygame, player, enemies


plr = player.Player(5, 2, 1, 0, Image(76*4, 61*4, "images\\portrats\\player.png", 24, 32))

# ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"]

def test():
    print("Hello world")

button_attack = Buttons(133,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],99*4,97*4,test)

button_heal =Buttons(133,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],133*4,97*4,test)

button_deffence = Buttons(133,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],167*4,97*4,test)

heart_icon = Image(16*4, 16*4, "images\\icons\\hp.png", 6*4, 70*4)
shield_icon = Image(16*4, 16*4, "images\\icons\\shield.png", 36*4, 70*4)
sword_icon = Image(16*4, 16*4, "images\\icons\\sword.png", 66*4, 70*4)
 
hp_message = Text(24,324,50,'Comic Sans',"HP",(0,0,0)) 
Def_message = Text(130,324,50,'Comic Sans',"DEF",(0,0,0))
Att_message = Text(235,324,50,'Comic Sans',"ATT",(0,0,0))