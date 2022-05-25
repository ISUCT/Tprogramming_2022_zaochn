from unittest import TestCase
import function as function

class TestFunction(TestCase):
    
    def test_f(self):
        res = function.f(2.0, 3.0, 0.11)
        self.assertAlmostEqual(1.58, res, 2)

    def test_f_zero(self):
        res = function.f(2.0, 3.0, 0)
        self.assertAlmostEqual(1.57, res, 2)

    def test_task_a_ok(self):
        y = function.task_a(2.0, 3.0, 0.11, 0.36, 0.05)
        self.assertAlmostEqual(5, len(y))

    def test_task_b_ok(self):
        y = function.task_b(2.0, 3.0, (0.08, 0.26, 0.35, 0.41, 0.53))
        self.assertAlmostEqual(5, len(y))

    def test_task_a(self):
        y = function.task_a(2.0, 3.0, 0.11, 0.36, 0.05)
        right_y = [1.58, 1.59, 1.61, 1.62, 1.64]
        for i in range(5):
            self.assertAlmostEqual(y[i], right_y[i], 2)

    def test_task_b(self):
        y = function.task_b(2.0, 3.0, (0.08, 0.26, 0.35, 0.41, 0.53))
        right_y = [1.58, 1.62, 1.65, 1.67, 1.71]
        for i in range(5):
            self.assertAlmostEqual(right_y[i], y[i], 2)