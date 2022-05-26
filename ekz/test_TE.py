import unittest
import TE

class TestTe(unittest.TestCase):
    def test_normal(self):
        expected= '1\n2\n3\n4\n5\n'
        result = TE.deistvie(1,5)
        self.assertEqual(expected, result)

5    def test_null(self):
        xk = 0
        expected= ''
        result = TE.deistvie(1,xk)
        self.assertEqual(expected,result)


if __name__ == "__main__":
    unittest.main()