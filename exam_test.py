from unittest import TestCase
import exam

class TableTest(TestCase):

    def test_a1_e_an(self):
        self.assertEqual(0, exam.table(2, 2, 1, 10))

    def test_b1_e_bn(self):
        self.assertEqual(0, exam.table(1, 10, 2, 2))

    def test_a1_gt_an(self):
        self.assertEqual(0, exam.table(20, 2, 1, 10))

    def test_b1_gt_bn(self):
        self.assertEqual(0, exam.table(1, 10, 20, 2))

    def test_a1_gt_an_is_negative(self):
        self.assertEqual(0, exam.table(-1, -10, 1, 10))

    def test_b1_gt_bn_is_negative(self):
        self.assertEqual(0, exam.table(1, 10, -1, -10))

    def test_a_is_negative(self):
        self.assertEqual(81, exam.table(-10, -1, 1, 10))
    
    def test_b_is_negative(self):
        self.assertEqual(81, exam.table(1, 10, -10, -1))
    
    def test_normal(self):
        self.assertEqual(81, exam.table(1, 10, 1, 10))

    def test_one(self):
        self.assertEqual(1, exam.table(2, 3, 3, 4))