import unittest
import task

class TestTask(unittest.TestCase):
    
    def test_calc(self):
        res = task.calc(2.5, 4.6, 1.15)
        self.assertAlmostEqual(61.47, res, 2)
    
    def test_calc_zeros(self):
        res = task.calc(2.5, 4.6, 0)
        self.assertAlmostEqual(0.13, res, 2)
    
    def test_task_a_ok(self):
        x, y = task.task_a(2.5, 4.6, 0, 0.5, 0.1)
        self.assertEqual(6, len(x))
        self.assertEqual(6, len(y))
    
    def test_task_a_xk_lt_xn(self):
        x, y = task.task_a(2.5, 4.6, 1, 0, 0.1)
        self.assertEqual(0, len(x))
        self.assertEqual(0, len(y))
    
    def test_task_a_dx_gt_xk(self):
        x, y = task.task_a(2.5, 4.6, 0, 1, 10)
        self.assertEqual(1, len(x))
        self.assertEqual(1, len(y))
    
    def test_task_b_ok(self):
        x = [0, 0.1 , 0.2, 0.3]
        y = task.task_b(2.5, 4.6,x)
        self.assertEqual(len(x), len(y))
    
    def test_task_b_empty(self):
        x = []
        y = task.task_b(2.5, 4.6,x)
        self.assertEqual(0, len(y))


if __name__ == '__main__':
    unittest.main()