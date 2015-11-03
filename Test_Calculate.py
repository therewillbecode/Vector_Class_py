__author__ = 'Tom'
import unittest
from index import a, b
from index import Vector

short = Vector([1, 2])

class Test__init__(unittest.TestCase):
    def test_instantiation_successful(self):
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
