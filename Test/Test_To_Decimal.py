import unittest
from index import to_decimal


class Testto_decimal(unittest.TestCase):

    def test_decimal_conversion(self):
        self.assertEqual(to_decimal("0"), 0)

    def test_decimal_conversion2(self):
        self.assertEqual(to_decimal("1"), 1)

    def test_decimal_conversion8(self):
        self.assertEqual(to_decimal("100"), 4)

    def test_decimal_conversion3(self):
        self.assertEqual(to_decimal("1111111"), 127)

    def test_decimal_conversion88(self):
        self.assertEqual(to_decimal("1111011"), 123)

    def test_decimal_conversion838(self):
        self.assertEqual(to_decimal("0000"), 0)

    def test_decimal_conversion838(self):
        self.assertEqual(to_decimal("0001"), 1)

    def test_decimal_conversion848(self):
        self.assertEqual(to_decimal("1000"), 8)

    def test_decimal_conversion4(self):
        self.assertEqual(to_decimal("01010101001110011100000"), 2792672)
