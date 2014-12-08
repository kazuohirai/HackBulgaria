from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor

    def attack(self):
        if self.weapon is None:
            return 0
        if self.weapon.critical_hit() is True:
            return self.berserk_factor*self.weapon.damage*2
        return self.berserk_factor*self.weapon.damage
