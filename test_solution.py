import unittest
import pandas as pd
from solution import calculate_intersection

class TestSolution(unittest.TestCase):
    file_name = "./mock_cumulative.csv"
    def test_calculate_intersection(self):
        df = pd.read_csv(self.file_name, index_col=0)
        result = calculate_intersection(df)
        expected = [9260.0, 187.0]
        self.assertEqual(result, expected, f'Should be {expected}')


if __name__ == '__main__':
    unittest.main()