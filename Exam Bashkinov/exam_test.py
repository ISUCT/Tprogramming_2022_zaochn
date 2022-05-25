from unittest import TestCase
import exam

class SummTest(TestCase):

    def test_empty_args(self):
        self.assertEqual(4, exam.summ()) # Тестируем без аргументов

    def test_one_args(self):
        self.assertEqual(12, exam.summ(10)) # Тестируем с 1 аргументом

    def test_two_args(self):
        self.assertEqual(6, exam.summ(3, 3)) # Тестируем с 2 аргументами

    def test_a_zero(self):
        self.assertEqual(3, exam.summ(0, 3)) # Тестируем первый аргумент 0

    def test_b_zero(self):
        self.assertEqual(3, exam.summ(3, 0)) # Тестируем второй аргумент 0
    
    def test_two_zero(self):
        self.assertEqual(0, exam.summ(0, 0)) # Тестируем оба аргумента 0

    def test_only_b(self):
        self.assertEqual(22, exam.summ(b=20)) # Тестируем указываем только 2 аргумент
