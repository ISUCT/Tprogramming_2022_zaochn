from unittest import TestCase
import Lab_1.function as function

class TestFunction(TestCase):
    
    def test_f(self):
        res = function.f(1.1, 0.09, 1.2)
        self.assertAlmostEqual(-3.29, res, 2)

    def test_task_a_ok(self):
        y = function.task_a(1.1, 0.09, 1.2, 2.2, 0.2)
        self.assertAlmostEqual(6, len(y))

    def test_task_b_ok(self):
        y = function.task_b(1.1, 0.09, (1.21, 1.76, 2.53, 3.48, 4.52))
        self.assertAlmostEqual(5, len(y))

    def test_task_a(self):
        y = function.task_a(1.1, 0.09, 1.2, 2.2, 0.2)
        right_y = [-3.291, -0.0905, 0.714, 1.042, 1.210, 1.308]
        for i in range(5):
            self.assertAlmostEqual(y[i], right_y[i], 3)

    def test_task_b(self):
        y = function.task_b(1.1, 0.09, (1.21, 1.76, 2.53, 3.48, 4.52))
        right_y = [-2.948, 0.994, 1.4, 1.501, 1.536]
        for i in range(5):
            self.assertAlmostEqual(right_y[i], y[i], 3)