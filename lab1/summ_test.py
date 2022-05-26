import unittest
import exam

class TestSumm(unittest.TestCase):

    def test_positive(self):
        res = exam.summ(15, 20)
        self.assertEqual(res)
    
    def test_negative(self):
        res = exam.summ(-15, -20)
        self.assertEqual(res)
    
    def test_first_negative(self):
        res = exam.summ(-15, 20)
        self.assertEqual(res)

    def test_second_negative(self):
        res = exam.summ(15, -20)
        self.assertEqual(res)

    def test_zero(self):
        res = exam.summ(0, 0)
        self.assertEqual(res)

    def test_positive(self):
        res = exam.summ(10, 15)
        self.assertEqual(res)
if __name__ == '__main__':
    unittest.main()