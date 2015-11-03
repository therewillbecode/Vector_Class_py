__author__ = 'Tom'
import unittest
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')

from index import a, b
from index import Vector


class Test__init__(unittest.TestCase):
    def test_length_property(self):
        self.assertEqual(a.length, 3)


class Test__str__(unittest.TestCase):
    def test_(self):
        self.assertEqual(a.length, 1)

class Test_Add(unittest.TestCase):
    pass

class Test_Subtract(unittest.TestCase):
    pass


class Test_Norm(unittest.TestCase):
    pass


class Test_Dot(unittest.TestCase):
    pass