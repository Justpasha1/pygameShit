import pygame, os, constans, buttons, random

class Player:
    def __init__(self, hp, dmg, df, gold):
        self.HitPoints=hp
        self.CurHP = self.HitPoints
        self.Damage=dmg
        self.Defense=df
        self.CurDefense = 0
        self.Gold=gold
        self.CritChance = 25
    def attack(self):
        pass
    def defense(self):
        pass
    def heal(self):
        pass
    def buy(self):
        pass
    def earn(self):
        pass
    def attacked(self):
        pass