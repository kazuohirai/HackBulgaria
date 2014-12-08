import unittest
from goldbach import goldbach


class testGoldbach(unittest.TestCase):

    def test_if_input_is_correct(self):
        self.assertFalse(goldbach(5))
        self.assertFalse(goldbach(1))
        self.assertFalse(goldbach(-10))
        self.assertFalse(goldbach(-1543))

    def test_if_outhput_is_correct(self):
        result = goldbach(100)
        self.assertEqual(
            result, [(3, 97), (11, 89), (17, 83),
                     (29, 71), (41, 59), (47, 53)])
        result2 = goldbach(10)
        self.assertEqual(result2, [(3, 7), (5, 5)])

if __name__ == "__main__":
    unittest.main()
