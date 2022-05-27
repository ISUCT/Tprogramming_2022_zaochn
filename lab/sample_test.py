import unittest
import sample

class TestSumm(unittest.TestCase):

    def test_3(self):
        res = sample.table(3)
        exp = '''1\t2\t3\t
2\t4\t6\t
3\t6\t9\t
'''
        self.assertEqual(exp, res)
    
    def test_zero(self):
        res = sample.table(0)
        exp = ''
        self.assertEqual(exp, res)

    def test_negative(self):
        res = sample.table(-4)
        exp = ''
        self.assertEqual(exp, res)
    
if __name__ == '__main__':
    unittest.main()