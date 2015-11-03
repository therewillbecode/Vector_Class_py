__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')
from index import a, b
from index import Vector

short = Vector([1, 2])

class Test_Error_Unequal_Length(unittest.TestCase):

    def test_raiseError_for_unequal_length(self):
        self.assertRaises(AttributeError, lambda: short.norm(a))

    def test_raiseError_for_unequal_length(self):
        self.assertRaises(AttributeError, lambda: short.dot(a))

    def test_raiseError_for_unequal_length(self):
        self.assertRaises(AttributeError, lambda: short.norm(a))

    def test_raiseError_for_unequal_length(self):
        self.assertRaises(AttributeError, lambda: short.add(a))

    def test_raiseError_for_unequal_length(self):
        self.assertRaises(AttributeError, lambda: short.subtract(a))
