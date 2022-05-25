from unittest import TestCase
import exam

class Lt5Test(TestCase):

    def test_empty(self):
        self.assertEqual([], exam.lt5([]))

    def test_from_1_to_10(self):
        self.assertEqual([1, 2, 3, 4], exam.lt5([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_from_5_to_10(self):
        self.assertEqual([], exam.lt5([5, 6, 7, 8, 9]))

    def test_with_str(self):
        self.assertEqual([], exam.lt5(['1' '2', '3', '4', '5', '6', '7', '8', '9']))

    def test_with_float(self):
        self.assertEqual([1.0, 2.0, 3.0, 4.0], exam.lt5([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]))

    def test_is_neagtive(self):
        self.assertEqual([-1, -2, -3, -4, -5, -6, -7, -8, -9], exam.lt5([-1, -2, -3, -4, -5, -6, -7, -8, -9]))
