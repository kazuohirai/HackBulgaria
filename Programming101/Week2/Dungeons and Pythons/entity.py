class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, dp):
        if self.health - dp > 0:
            self.health -= dp
        else:
            self.health = 0

    def take_healing(self, hp):
        if self.health == 0:
            self.health = 0
        elif self.health + hp < self._MAX_HEALTH:
            self.health += hp
        else:
            self.health = self._MAX_HEALTH

    def has_weapon(self):
        if self.weapon is not None:
            return True
        return False

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            return 0
        else:
            return self.weapon.damage
