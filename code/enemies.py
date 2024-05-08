from pygame import *
from superclasses import *
class Enemies(Creatures):
    def __init__(self, hp: int, dmg: int, df: int, gold: int, portrait: Image, func:callable):
        super().__init__(hp, dmg, df, gold, portrait)
        self.Func = func
    def Use_special(self):
        self.Func()