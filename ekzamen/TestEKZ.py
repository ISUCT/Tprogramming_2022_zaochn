from random import ekz
import unittest
import ekz

class TestTask(unittest.TestCase):
   
   def test_3(self):
       res = ekz.table(3)
       exp = '''1\t2\t3\t
2\t4\t6\t
3\t6\\t9\t       
'''
       self.assertEqual(exp, res)

   def test_zero(self):
        res = ekz.table(0)
        exp = ''
        self.assertEqual(exp, res)

   def test_negative(self):
        res = ekz.table(-4)
        exp = ''
        self.assertEqual(exp, res)

if __name__ == '__main__':
    unittest.main()