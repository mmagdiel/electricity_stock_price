import unittest
from helpers import get_determinant, get_line_equation, get_pairs, get_intersection_lines

class TestDeterminant(unittest.TestCase):

    def test_negative(self):
        result = get_determinant([2, 3], [3, 2])
        expected = -5 
        self.assertEqual(result, expected, f'Should be {expected}')

    def test_positive(self):
        result = get_determinant([3, 2], [2, 3])
        expected = 5 
        self.assertEqual(result, expected, f'Should be {expected}')

    def test_zero(self):
        result = get_determinant([3, 2], [6, 4])
        expected = 0 
        self.assertEqual(result, expected, f'Should be {expected}')


class TestGetLineEquation(unittest.TestCase):

    def test_some_line(self):
        result = get_line_equation([-3, 2], [5,-1])
        expected = [0.375, 1, -0.875]
        self.assertEqual(result, expected, f'Should be {expected}')

    def test_another_line(self):
        result = get_line_equation([2, 3], [4, 6])
        expected = [-1.5, 1, 0]
        self.assertEqual(result, expected, f'Should be {expected}')


    def test_another_line(self):
        result = get_line_equation([2, 3], [2, 6])
        expected = [2, 0, 0]
        self.assertEqual(result, expected, f'Should be {expected}')


class TestGetPairs(unittest.TestCase):

    def test_pair_default_1(self):
        result = get_pairs([-3, 2])
        expected = [-3, 2]
        self.assertEqual(result, expected, f'Should be {expected}')
    
    def test_pair_default_2(self):
        result = get_pairs([-3, 2, 1, 4])
        expected = [-3, 2]
        self.assertEqual(result, expected, f'Should be {expected}')

    def test_pair_selected(self):
        result = get_pairs([-3, 2, 4], 2, 1, -1)
        expected = [-4, 2]
        self.assertEqual(result, expected, f'Should be {expected}')

    def test_pair_default_2(self):
        result = get_pairs([-3, 2, 4], 2, 0, -1)
        expected = [-4, -3]
        self.assertEqual(result, expected, f'Should be {expected}')

class TestGetIntersectionLines(unittest.TestCase):

    def test_pair_default_1(self):
        result = get_intersection_lines([2, 3, -5], [3, 2, 1])
        expected = [-2.6, 3.4]
        self.assertEqual(result, expected, f'Should be {expected}')


if __name__ == '__main__':
    unittest.main()