import unittest
import home_job


class TestSumm(unittest.TestCase):

    def test_positive(self):
        res = home_job.summ(2, 3)
        self.assertEqual(5, res)

    def test_negative(self):
        res = home_job.summ(-2, -3)
        self.assertEqual(-5, res)

    def test_first_negative(self):
        res = home_job.summ(-2, 3)
        self.assertEqual(1, res)

    def test_second_negative(self):
        res = home_job.summ(2, -3)
        self.assertEqual(-1, res)

    def test_zero(self):
        res = home_job.summ(0, 0)
        self.assertEqual(0, res)


if __name__ == '__main__':
    unittest.main()
