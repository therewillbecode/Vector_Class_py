__author__ = 'Tom'
import unittest
from index import calculate


class Testcalculate(unittest.TestCase):

    def test_should_give_one(self):
        self.assertEqual(calculate("1", ""), 1)

    def test_should_give_2(self):
        self.assertEqual(calculate("1", "1"), 2)

    def test_decimal_conversion9(self):
        self.assertEqual(calculate("10", "10"), 4)

    def test_decimal_conversion99(self):
        self.assertEqual(calculate("101", "100"), 9)

    def test_f(self):
        self.assertEqual(calculate("1010101", "1010101"), 170)