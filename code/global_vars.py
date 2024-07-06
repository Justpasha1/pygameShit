from random import randint
from buttons import *
from superclasses import *
import pygame, player, enemies, superclasses


plr = player.Player(5, 2, 1, 0, Image(76*4, 61*4, "images\\portrats\\player.png", 24, 32))

# ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"]

heart_icon = Image(16*4, 16*4, "images\\icons\\hp.png", 6*4, 70*4)
shield_icon = Image(16*4, 16*4, "images\\icons\\shield.png", 36*4, 70*4)
sword_icon = Image(16*4, 16*4, "images\\icons\\sword.png", 66*4, 70*4)

hp_message = Text(41,324,50, 'Comic Sans', plr.HitPoints, (0,0,0)) 
Def_message = Text(164,324,50, 'Comic Sans', plr.Defense, (0,0,0))
Att_message = Text(287,324,50, 'Comic Sans', plr.Damage, (0,0,0))

def test():
        print("Hello world")

#Enemies
succubus = enemies.Enemies(4, 2, 0, 10, Image(40*4, 56*4, "images\\portrats\\enemy\\fuck_up_succubus.png", 125*4, 17*4 ), test)

cur_enemy = succubus

def Attack(Damage, cur_enemy):
        cur_enemy.attacked(Damage)
def Heal(amount):
        plr.heal(amount)
        hp_message.Text = str(plr.CurHP)
        hp_message.convert()
def Defence(Defense):
        plr.defence(Defense)
        Def_message.Text = str(plr.Defense)
        Def_message.convert()

button_attack = Buttons(133,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],99*4,97*4, lambda: Attack(plr.Damage, cur_enemy))
button_heal =Buttons(133,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],133*4,97*4, lambda: Heal(randint(-1, 2)))
button_deffence = Buttons(133,150, ["images\\buttons\\rectangle\\base.png","images\\buttons\\rectangle\\hover.png", "images\\buttons\\rectangle\\pressed.png"],167*4,97*4,Defence)