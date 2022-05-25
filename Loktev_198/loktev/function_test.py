from unittest import TestCase
import function as function

class TestFunction(TestCase):
    
    def test_f(self):
        res = function.f(1.2, 0.48, 0.7)
        self.assertAlmostEqual(0.36, res, 2)

    def test_f_zero(self):
        res = function.f(1.2, 0.48, 0)
        self.assertAlmostEqual(0.043, res, 3)

    def test_task_a_ok(self):
        y = function.task_a(1.2, 0.48, 0.7, 2.2, 0.3)
        self.assertAlmostEqual(5, len(y))

    def test_task_b_ok(self):
        y = function.task_b(1.2, 0.48, (0.25, 0.36, 0.56, 0.94, 1.28))
        self.assertAlmostEqual(5, len(y))

    def test_task_a(self):
        y = function.task_a(1.2, 0.48, 0.7, 2.2, 0.3)
        right_y = [0.361, 0.584, 0.708, 0.661, 0.468] 
        for i in range(5):
            self.assertAlmostEqual(y[i], right_y[i], 3)

    def test_task_b(self):
        y = function.task_b(1.2, 0.48, (0.25, 0.36, 0.56, 0.94, 1.28))
        right_y = [0.09, 0.13, 0.26, 0.54, 0.7]
        for i in range(5):
            self.assertAlmostEqual(right_y[i], y[i], 2)