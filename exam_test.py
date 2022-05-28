from unittest import TestCase
import exam

class PalindromTest(TestCase):

    def test_palindrom_word_even(self):
        self.assertTrue(exam.is_palindrom('werrew')) # Тестируем слово палиндром с чётным количеством символов
        
    def test_palindrom_word_odd(self):
        self.assertTrue(exam.is_palindrom('werew')) # Тестируем слово не палиндром

    def test_not_palindrom_word(self):
        self.assertFalse(exam.is_palindrom('qwerty')) # Тестируем слово палиндром с нечётным кол-вом символов

    def test_frase_palindrom(self):
        self.assertTrue(exam.is_palindrom('Sator arepo tenet opera rotas')) # Тестируем фразу палиндром
    
    def test_frase_not_palindrom(self):
        self.assertFalse(exam.is_palindrom('One two three')) # Тестируем фразу не палиндром

    def test_digit_palindrom_even(self):
        self.assertTrue(exam.is_palindrom('123321')) # Тестируем палиндром из цифр с чётным кол-вом символов

    def test_digit_palindrom_odd(self):
        self.assertTrue(exam.is_palindrom('12321')) # Тестируем палиндром из цифр с нечётным кол-вом символов

    def test_digit_not_palindrom(self):
        self.assertFalse(exam.is_palindrom('123456')) # Тестируем не палиндром из цифр 