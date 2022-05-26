import unittest
import home_job


class TestExample(unittest.TestCase):

    def test_example(self):
        res = home_job.example(2, 0.95, 1.25)
        self.assertAlmostEqual(-0.35, res, 2)

    def test_example_zeros(self):
        res = home_job.example(2, 0.95, 1)
        self.assertAlmostEqual(-0.0, res, 2)

    def test_example_a_ok(self):
        x, y = home_job.example_a(2, 0.95, 0.1, 0.6, 0.1)
        self.assertEqual(6, len(x))
        self.assertEqual(6, len(y))

    def test_example_a_xk_lt_xn(self):
        x, y = home_job.example_a(2, 0.95, 1, 0, 0.1)
        self.assertEqual(0, len(x))
        self.assertEqual(0, len(y))

    def test_example_a_dx_gt_xk(self):
        x, y = home_job.example_a(2, 0.95, 0.1, 1, 10)
        self.assertEqual(1, len(x))
        self.assertEqual(1, len(y))

    def test_example_b_ok(self):
        x = [0.01, 0.1 , 0.2, 0.3]
        y = home_job.example_b(2, 0.95, x)
        self.assertEqual(len(x), len(y))

    def test_example_b_empty(self):
        x = []
        y = home_job.example_b(2, 0.95,x)
        self.assertEqual(0, len(y))


if __name__ == '__main__':
    unittest.main()
