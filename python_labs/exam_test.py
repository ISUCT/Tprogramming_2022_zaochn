# тут я попытался написать хоть какие-то тесты, но почему-то получаю ошибку 'str' object is not callable

import unittest
import exam

class TestExam(unittest.TestCase):

    def test_a_is_palindrome(self):
        assert exam.a("A") is True
        assert exam.a("LOL") is True
        assert exam.a("racecar") is True

if __name__ == "__main__":
    unittest.main()
