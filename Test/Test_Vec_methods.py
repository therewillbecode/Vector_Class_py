__author__ = 'Tom'
import unittest
import sys
import mock
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Tom/PycharmProjects/vector_class/Vector_Calc_py')

from index import a, b
from index import Vector
unittest.mock

class __init__(unittest.TestCase):
    def test_length_property(self):
        self.assertEqual(a.length, 3)

class __str__(unittest.TestCase):
    def test_(self):
        self.assertEqual(str(a), '(1,2,3)')

class Add(unittest.TestCase):

    def test_returns_vector_object(self):
        self.assertEqual(a.array, [4, 6, 8])

    def test_adds_properly(self):
        self.assertEqual(a.__class__.__name__, 'Vector' )

class Subtract(unittest.TestCase):
    pass


class Norm(unittest.TestCase):
    pass


class Dot(unittest.TestCase):
    pass