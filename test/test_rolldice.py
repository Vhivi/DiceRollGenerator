import unittest
from main import roll_dice

class TestRollDice(unittest.TestCase):
    def test_roll_dice(self):
        # Test rolling 2 dice with 6 faces
        result = roll_dice(2, 6)
        self.assertEqual(len(result), 2)
        for roll in result:
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    def test_roll_dice_invalid_input(self):
        # Test rolling with invalid input
        with self.assertRaises(ValueError):
            roll_dice(0, 6)
        with self.assertRaises(ValueError):
            roll_dice(2, 3)
        with self.assertRaises(ValueError):
            roll_dice(-1, 6)
        with self.assertRaises(ValueError):
            roll_dice(2, -4)
        with self.assertRaises(ValueError):
            roll_dice(1.5, 6)
        with self.assertRaises(ValueError):
            roll_dice(2, 4.5)
        with self.assertRaises(ValueError):
            roll_dice("2", 6)
        with self.assertRaises(ValueError):
            roll_dice(2, "6")

if __name__ == '__main__':
    unittest.main()