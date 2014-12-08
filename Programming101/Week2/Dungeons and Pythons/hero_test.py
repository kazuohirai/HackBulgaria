import unittest
from hero import Hero


class TestHero(unittest.TestCase):
    def test_hero_known_as_not_Jenkins(self):
        self.bron_hero = Hero("Bron", 100, "Dragon Slayer")
        self.assertEqual(self.bron_hero.known_as(), "Bron the Dragon Slayer")

    def test_hero_known_as_Jenkins(self):
        self.leeroy = Hero("Leeroy", 100, "Jenkins")
        self.assertEqual(self.leeroy.known_as(), "Leeroy Jenkins")

if __name__ == "__main__":
    unittest.main()
