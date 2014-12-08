import unittest
from entity import Entity
from weapon import Weapon


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.character = Entity("Arthas", 100)
        self.char = Entity("Gancho", 100)
        self.character.weapon = Weapon("Frostmourne", 100, 0.9)
        self.weapon = Weapon("Stick", 5, 0.1)

    def test_hero_init(self):
        self.assertEqual(self.character.name, "Arthas")
        self.assertEqual(self.character.health, 100)
        self.assertEqual(self.character.weapon.name, "Frostmourne")

    def test_get_health(self):
        self.assertEqual(100, self.character.get_health())

    def test_is_alive(self):
        self.assertTrue(self.character.is_alive())

    def test_is_not_alive(self):
        self.character.health = 0
        self.assertFalse(self.character.is_alive())

    def test_damage_deal_if_player_is_alive(self):
        self.character.take_damage(30)
        self.assertEqual(70, self.character.health)

    def test_damage_deal_if_player_is_dead(self):
        self.character.health = 70
        self.character.take_damage(70)
        self.assertEqual(0, self.character.health)

    def test_regular_heal(self):
        self.character.health = 50
        self.character.take_healing(20)
        self.assertEqual(70, self.character.health)

    def test_healing_if_dead(self):
        self.character.health = 0
        self.character.take_healing(20)
        self.assertEqual(0, self.character.health)

    def test_healing_if_full(self):
        self.character.health = self.character._MAX_HEALTH
        self.character.take_healing(20)
        self.assertEqual(100, self.character.health)

    def test_if_entity_has_weapon(self):
        self.assertTrue(self.character.has_weapon())

    def test_if_entity_is_unarmed(self):
        self.assertFalse(self.char.has_weapon())

    def test_if_equips_unarmed_person(self):
        self.char.equip_weapon(self.weapon)
        self.assertEqual(self.weapon, self.char.weapon)

    def test_if_equips_new_weapon(self):
        self.character.equip_weapon(self.weapon)
        self.assertEqual(self.weapon, self.character.weapon)

    def test_damage_of_entity_with_weapon(self):
        self.assertEqual(self.character.attack(), 100)

    def test_damage_of_entity_without_weapon(self):
        self.assertEqual(self.char.attack(), 0)


if __name__ == "__main__":
    unittest.main()
