import random


class Weapon:
    def __init__(self, name, damage, critChance):
        self.name = name
        self.damage = damage
        self.__set_critical_strike_percentage(critChance)

    def __set_critical_strike_percentage(self, critChance):
        if critChance > 0 and critChance < 1.0:
            self.critChance = critChance
        else:
            raise ValueError

    def critical_hit(self):
        return random.random() <= self.critChance
