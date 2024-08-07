from pygame import *
from superclasses import *
import random

class Enemies(Creatures):
    def __init__(self, hp: int, dmg: int, df: int, gold: int, portrait: Image, func:callable):
        super().__init__(hp, dmg, df, gold, portrait)
        self.Func = func
        self.Actions = ["defence", "attack"]
        self.CurGoal = random.choice(self.Actions)
        self.Turn = 1 if self.CurGoal=="defence" else random.randint(2, 3)
    def Use_special(self):
        self.Func()