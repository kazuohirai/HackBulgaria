import unittest
from weapon import Weapon


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.test_weapon = Weapon("Wirt's Leg", 45, 0.9)

    def test_weapon_init(self):
        self.assertEqual(self.test_weapon.name, "Wirt's Leg")
        self.assertEqual(self.test_weapon.damage, 45)
        self.assertEqual(self.test_weapon.critChance, 0.9)

    def test_critical_hit_error_negative_crit(self):
        with self.assertRaises(ValueError):
            weapon = Weapon("Name", 10, -1)

    def test_critical_hit_error_bigger_crit(self):
        with self.assertRaises(ValueError):
            weapon = Weapon("Name", 10, 2)

    def test_critical_hit(self):
        results = []
        for i in range(0, 1000):
            results.append(self.test_weapon.critical_hit())
        self.assertEqual(2, len(set(results)))

if __name__ == "__main__":
    unittest.main()
