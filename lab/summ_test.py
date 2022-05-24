import unittest
import task

class TestSumm(unittest.TestCase):

    def test_positive(self):
        res = task.summ(2, 3)
        self.assertEqual(5, res)
    
    def test_negative(self):
        res = task.summ(-2, -3)
        self.assertEqual(-5, res)
    
    def test_first_negative(self):
        res = task.summ(-2, 3)
        self.assertEqual(1, res)

    def test_second_negative(self):
        res = task.summ(2, -3)
        self.assertEqual(-1, res)

    def test_zero(self):
        res = task.summ(0, 0)
        self.assertEqual(0, res)

if __name__ == '__main__':
    unittest.main()
