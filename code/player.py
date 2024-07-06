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
    