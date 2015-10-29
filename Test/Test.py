import unittest
from index import to_decimal

class decimal_conversion(unittest.TestCase):

    def one_should_convert_to_one(self):
        Test.assert_equals(to_decimal("1"), 1)
