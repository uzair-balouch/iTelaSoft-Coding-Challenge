import unittest
import iTelaSoft_coding_challenge

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(iTelaSoft_coding_challenge.correct_cost(), 4140, "Should be 4140")

if __name__ == '__main__':
    unittest.main()