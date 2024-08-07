from superclasses import Image
import pygame, os, constans, buttons, random
from superclasses import *

class Player(Creatures):
    def __init__(self, hp: int, dmg: int, df: int, gold: int, portrait: Image):
        super().__init__(hp, dmg, df, gold, portrait)
        self.Effects = []
    def heal(self, amount):
        if self.CurHP+amount>self.HitPoints:
            CurHP=5
        else:
            self.CurHP+=amount

    def can_buy(self, amount):
        if self.Gold - amount < 0:
            return False
        else:
            self.Gold -= amount
            return True
    def earn(self, enemy_gold):
        self.Gold+=enemy_gold
    def attacked(self, damage):
        if damage>self.CurDefence:
            self.CurHP-=damage-self.CurDefence
            print(self.CurHP)
            self.CurDefence=0
    def attack(self, enemy):
        if self.Damage>enemy.CurDefence:
            enemy.CurHP-=self.Damage-enemy.CurDefence
            enemy.CurDefence=0
        else:
            enemy.CurDefence-=self.Damage
        print(f" ememy Defence: {enemy.CurDefence} \n enemy HP {enemy.CurHP}")
    def make_turn(self, enemy):
        enemy.Turn -= 1
        if  enemy.Turn == 0:
            if enemy.CurGoal == "attack":
                self.attacked(enemy.Damage)
            elif enemy.CurGoal == "defence":
                enemy.defece()
            self.Defence = 0
            enemy.CurGoal = random.choice(enemy.Actions)
            enemy.Turn = 1 if enemy.CurGoal=="defence" else random.randint(2, 3)