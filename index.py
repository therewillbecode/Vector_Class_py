__author__ = 'Tom'
import math

class Vector:
    def __init__(self, arr):
        self.array = arr
        self.length = len(arr)

    def __str__(self):
        pass

    def add(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")

    def subtract(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")

    def dot(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")

    def norm(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")



a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

print(a.add(b))

