import unittest
from main import roll_dice, validate_input

class TestRollDice(unittest.TestCase):
    def test_roll_dice(self):
        # Test roll_dice function with valid inputs
        num_dice = 2
        num_faces = 6
        results = roll_dice(num_dice, num_faces)
        self.assertEqual(len(results), num_dice)
        for result in results:
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, num_faces)

    def test_roll_dice_invalid_input(self):
        # Test roll_dice function with invalid inputs
        num_dice = 0
        num_faces = 6
        with self.assertRaises(ValueError):
            roll_dice(num_dice, num_faces)

        num_dice = 2
        num_faces = 3
        with self.assertRaises(ValueError):
            roll_dice(num_dice, num_faces)

if __name__ == '__main__':
    unittest.main()