import unittest
import exam

class TestExam(unittest.TestCase):

    def test_example(self):
        res = exam.elements([1, 2, 3])
        self.assertAlmostEqual(3, res)


if __name__ == '__main__':
    unittest.main()