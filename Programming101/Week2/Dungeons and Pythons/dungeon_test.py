import unittest
from dungeon import Dungeon
from hero import Hero
from orc import Orc
import os


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.filename = "maze.txt"
        self.contents = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S"
        with open(self.filename, "w+") as f:
            f.write(self.contents)
            f.close()

        self.peshtera = Dungeon("maze.txt")
        self.orc = Orc("Ivancho", 100, 1.3)
        self.hero = Hero("Petarcho", 100, "Garbage")

    def tearDown(self):
        os.remove(self.filename)

    def test_dungeon_map(self):
        with open(self.filename, "r+") as f:
            actual = f.read()
            f.close()
        self.assertEqual(self.contents, actual)

    def test_print_map(self):
        output = self.peshtera.print_map()
        with open(self.filename, "r+") as f:
            actual = f.read()
            f.close()
        self.assertEqual(output, actual)

    def test_spawn_character(self):
        self.peshtera.spawn("Player One", self.orc)
        with open(self.filename, "r+") as f:
            actual = f.read()
            f.close()
        contents = "O.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S"
        self.assertEqual(actual, contents)

    def test_spawn_already_spawned_character(self):
        self.peshtera.spawnlist = {"Player One": self.orc}
        result = self.peshtera.spawn("Player One", self.orc)
        self.assertEqual("Character is already spawned.", result)

    def test_spawn_with_no_free_slots(self):
        self.filename = "maze.txt"
        self.contents = "..##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####."
        with open(self.filename, "w+") as f:
            f.write(self.contents)
            f.close()
        result = self.peshtera.spawn("One", self.orc)
        self.assertEqual("No free spawn slot.", result)

    def test_move_to_unknown_given_direction(self):
        self.peshtera.spawn("Orc", self.orc)
        result = self.peshtera.move("Orc", "test")
        self.assertEqual("Wrong direction given.", result)


if __name__ == "__main__":
    unittest.main()
