import unittest
from linear_regression import *

class TestLinearRegressionFunctions(unittest.TestCase):
    # Test the get_y function
    def test_get_y(self):
        self.assertEqual(get_y(2, 3, 4), 11)  # Should return y = 2 * 4 + 3 = 11
        self.assertEqual(get_y(0, 5, 2), 5)   # Should return y = 0 * 2 + 5 = 5
        self.assertAlmostEqual(get_y(-1.5, 1.2, 0), 1.2) # Should return y = -1.5 * 0 + 1.2 = 1.2
        with self.assertRaises(ValueError):
            get_y("2", 3, 4)  # Should raise ValueError

    # Test the calculate_error function
    def test_calculate_error(self):
        point1 = (3, 5) # x = 3, y = 4
        point2 = (2, 2) # x = 6, y = 8

        self.assertEqual(calculate_error(2, 1, point1), 2) # y = 2 * 3 + 1 = 7, should return difference = |7 - 5| = 2
        self.assertEqual(calculate_error(1, 0, point2), 0) # y = 1 * 2 + 0 = 2, should return difference = |2 - 2| = 0
        self.assertAlmostEqual(calculate_error(-1.5, 1.2, (0, 1.2)), 0.0) # y = -1.5 * 0 + 1.2 = 1.2, should return difference = |1.2 - 1.2| = 0.0
        with self.assertRaises(ValueError):
            calculate_error("2", 3, (4, 11)) # Should raise ValueError

    #Test the calculate_all_error function
    def test_calculate_all_error(self):
        points = [(1, 2), (2, 0), (3, 4)]

        self.assertEqual(calculate_all_error(1, 1, points), 3)  # m=1, b=1, should return total_error = 3
        self.assertAlmostEqual(calculate_all_error(-1.5, 1.2, points), 11) # m=-1.5, b=1.2, should return total_error = 11
        with self.assertRaises(ValueError):
            calculate_all_error("2", 3, points) # Should raise ValueError
        with self.assertRaises(ValueError):
            calculate_all_error(2, 3, [(1, 2), (2, 0), (3, 4), (4, 4), 5, 3]) # Invalid point format

    #Test the find_smallest_error function
    def test_find_smallest_error(self):
        possible_ms = [1, 2]
        possible_bs = [0, 1]
        datapoints = [(1, 2), (2, 0), (3, 4)]
        custom_ms = [1, 2]
        custom_bs = [1, 2]
        best_m, best_b, smallest_error = find_smallest_error(possible_ms, possible_bs, datapoints, custom_ms, custom_bs)

        self.assertEqual(best_m, 1) # m=1, should return best_m = 1
        self.assertEqual(best_b, 1) # b=1, should return best_b = 1
        self.assertEqual(smallest_error, 3) # m=1, b=1, should return smallest_error = 3

        with self.assertRaises(ValueError):
            find_smallest_error([0.0, "1.0", 2.0], possible_bs, datapoints) # Invalid slope format
        with self.assertRaises(ValueError):
            find_smallest_error(possible_ms, [0.0, "1.0", 2.0], datapoints) # Invalid y-intercept format
        with self.assertRaises(ValueError):
            find_smallest_error(possible_ms, possible_bs, [(1, 1), (2, 2), (3, 3), 4, 4])  # Invalid point format
        with self.assertRaises(ValueError):
            find_smallest_error(possible_ms, possible_bs, datapoints, [0.0, "1.0", 2.0], custom_bs) # Invalid custom slope format
        with self.assertRaises(ValueError):
            find_smallest_error(possible_ms, possible_bs, datapoints, custom_ms, [0.0, "1.0", 2.0]) # Invalid custom y-intercept format

if __name__ == '__main__':
    unittest.main()
