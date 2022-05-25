import unittest
import task

class TestStringMethods(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(task.reverse_str('foo'), 'oof')

    def test_empty(self):
        self.assertEqual(task.reverse_str(''), '')

    def test_polyndrome(self):
        self.assertEqual(task.reverse_str('MAMAM'), 'MAMAM')

    def test_not_equal(self):
        self.assertNotEqual(task.reverse_str('123'), '123')

unittest.main()
