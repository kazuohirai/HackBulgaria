import unittest
from orc import Orc
from weapon import Weapon


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.orc = Orc("Thrall", 100, 1.5)
        self.bradva = Weapon("Axe", 16, 0.4)
        self.orc.weapon = self.bradva
        self.unarmedOrc = Orc("Unarmed", 100, 1.3)

    def test_init(self):
        self.assertEqual(self.orc.name, "Thrall")
        self.assertEqual(self.orc.health, 100)
        self.assertEqual(self.orc.berserk_factor, 1.5)

    def test_damage_if_entity_is_orc(self):
        self.assertIn(self.orc.attack(), [24, 48])

    def test_attack_if_orc_is_unequipped(self):
        result = self.unarmedOrc.attack()
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main()
