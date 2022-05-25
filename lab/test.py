import unittest;
import l1;

class TestTask(unittest.TestCase):
    def test_kghjy(self):
        res = l1.kghjy(0.05, 0.06, 0.15)
        self.assertAlmostEqual(77.59,res,2)

    def test_kghjy_zeros(self):
        res = l1.kghjy(0.05, 0.06, 0)
        self.assertAlmostEqual(-629.76, res,2)

if __name__ == '__main__':
    unittest.main()