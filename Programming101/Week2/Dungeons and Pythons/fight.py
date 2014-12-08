from random import randint


class Fight:
    def __init__(self, orc, hero):
        self.orc = orc
        self.hero = hero

    def simulate_fight(self):
        if self.hero.weapon is None and self.orc.weapon is None:
            return "No winner"
        (attacker, defender) = self.get_starting_character()

        while self.orc.is_alive() and self.hero.is_alive:
            damage = attacker.attack()
            defender.take_damage(damage)
            attacker, defender = defender, attacker

        if self.orc.is_alive():
            return self.orc
        return self.hero

    def get_starting_character(self):
        coin = randint(0, 100)
        if coin < 50:
            return (self.hero, self.orc)
        return (self.orc, self.hero)
