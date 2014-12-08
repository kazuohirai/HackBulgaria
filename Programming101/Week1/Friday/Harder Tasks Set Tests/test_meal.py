import unittest
from meal import prepare_meal


class TestMeal(unittest.TestCase):
    def test_with_multiples_of_neither_3_nor_5(self):
        result = prepare_meal(7)
        result2 = prepare_meal(8)
        result3 = prepare_meal(17)
        result4 = prepare_meal(23)
        self.assertEqual(result, "")
        self.assertEqual(result2, "")
        self.assertEqual(result3, "")
        self.assertEqual(result4, "")

    def test_with_divisibles_of_three_only(self):
        result = prepare_meal(3)
        result2 = prepare_meal(9)
        result3 = prepare_meal(27)
        result4 = prepare_meal(81)
        self.assertEqual(result, "spam")
        self.assertEqual(result2, "spam spam")
        self.assertEqual(result3, "spam spam spam")
        self.assertEqual(result4, "spam spam spam spam")

    def test_with_divisibles_of_five_only(self):
        result = prepare_meal(5)
        result2 = prepare_meal(25)
        result3 = prepare_meal(35)
        result4 = prepare_meal(55)
        self.assertEqual(result, "eggs")
        self.assertEqual(result2, "eggs")
        self.assertEqual(result3, "eggs")
        self.assertEqual(result4, "eggs")

    def test_with_divsibles_of_five_AND_three(self):
        result = prepare_meal(15)
        result2 = prepare_meal(45)
        result3 = prepare_meal(405)
        self.assertEqual(result, "spam and eggs")
        self.assertEqual(result2, "spam spam and eggs")
        self.assertEqual(result3, "spam spam spam spam and eggs")

if __name__ == "__main__":
    unittest.main()
