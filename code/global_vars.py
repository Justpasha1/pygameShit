from buttons import *
from superclasses import *
import pygame, player, enemies, superclasses


plr = player.Player(5, 2, 1, 0, Image(76*4, 61*4, "images\\portrats\\player.png", 24, 32))

# ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"]

def test():
        print("Hello world")
def Attack(Damage, cur_enemy_defence):
        cur_enemy_defence.attacked(Damage)
def Heal(amount):
        plr.heal(amount)
def Defence(Defense):
        plr.defence(Defense)

button_attack = Buttons(130,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],398,389,Attack)

button_heal = Buttons(130,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],529,389,Heal)

button_deffence = Buttons(130,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],660,389,Defence)

heart_icon = Image(16*4, 16*4, "images\\icons\\hp.png", 6*4, 70*4)
shield_icon = Image(16*4, 16*4, "images\\icons\\shield.png", 36*4, 70*4)
sword_icon = Image(16*4, 16*4, "images\\icons\\sword.png", 66*4, 70*4)

hp_message = Text(41,324,50, 'Comic Sans', plr.HitPoints, (0,0,0)) 
Def_message = Text(164,324,50, 'Comic Sans', plr.Defense, (0,0,0))
Att_message = Text(287,324,50, 'Comic Sans', plr.Damage, (0,0,0))


#Enemies
succubus = enemies.Enemies(4, 2, 0, 10, Image(40*4, 56*4, "images\\portrats\\enemy\\fuck_up_succubus.png", 125*4, 17*4 ), test)

