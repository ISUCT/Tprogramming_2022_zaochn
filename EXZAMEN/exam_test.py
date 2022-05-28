from unittest import TestCase
import exam

class ReversTest(TestCase):

    def test_zero_words(self):
        self.assertEqual('', exam.revers_word(''))
    
    def test_one_words(self):
        self.assertEqual('one', exam.revers_word('one'))

    def test_five_words(self):
        self.assertEqual('five four tree two one', exam.revers_word('one two tree four five'))

    def test_five_words_with_dot(self):
        self.assertEqual('five. four tree two One', exam.revers_word('One two tree four five.'))

    def test_five_words_sep_comma(self):
        self.assertEqual('five four, tree, two, one,', exam.revers_word('one, two, tree, four, five'))

    def test_five_words_sep_dash(self):
        self.assertEqual('one-two-tree-four-five', exam.revers_word('one-two-tree-four-five'))

    def test_ten_words_two_line(self):
        self.assertEqual('ten nine eight seven five\nsix four tree two one', exam.revers_word('one two tree four five\nsix seven eight nine ten'))

    def test_digit(self):
        self.assertEqual('5 4 3 2 1', exam.revers_word('1 2 3 4 5'))