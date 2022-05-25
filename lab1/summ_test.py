import unittest
import exam

class TestSumm(unittest.TestCase):

    def test_positive(self):
        res = exam.summ(15, 20)
        self.assertEqual(1, res)
    
    def test_negative(self):
        res = exam.summ(-15, -20)
        self.assertEqual(-1, res)
    
    def test_first_negative(self):
        res = exam.summ(-15, 20)
        self.assertEqual(1, res)

    def test_second_negative(self):
        res = exam.summ(15, -20)
        self.assertEqual(-1, res)

    def test_zero(self):
        res = exam.summ(0, 0)
        self.assertEqual(0, res)

if __name__ == '__main__':
    unittest.main()