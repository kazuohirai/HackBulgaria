import unittest
from hero import Hero
from orc import Orc
from fight import Fight
from weapon import Weapon


class TestFightingSkills(unittest.TestCase):
    def setUp(self):
        self.orc = Orc("Gerasim", 100, 1.7)
        self.hero = Hero("Spiridon", 100, "Lich King")
        self.bitka = Fight(self.orc, self.hero)
        self.orc.weapon = Weapon("Wirt's Leg", 30, 0.9)
        self.hero.weapon = Weapon("WarGlaive", 30, 0.5)

    def test_init_fighters(self):
        self.assertEqual(self.orc.name, "Gerasim")
        self.assertEqual(self.orc.health, 100)
        self.assertEqual(self.orc.berserk_factor, 1.7)
        self.assertEqual(self.hero.name, "Spiridon")
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.nickname, "Lich King")

    def test_simulate_fight(self):
        result = self.bitka.simulate_fight()
        self.assertIn(result, [self.orc, self.hero])

    def test_simulate_fight_with_no_weapon(self):
        self.orc.weapon = None
        result = self.bitka.simulate_fight()
        self.assertEqual(self.hero, result)

    def test_simulate_fight_with_unarmed_characters(self):
        self.orc.weapon = None
        self.hero.weapon = None
        result = self.bitka.simulate_fight()
        self.assertEqual(result, "No winner")

if __name__ == "__main__":
    unittest.main()
