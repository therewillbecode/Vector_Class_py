__author__ = 'Tom'
import math

class Vector:
    def __init__(self, arr):
        self.array = arr
        self.length = len(arr)

    def __str__(self):
        s = str(self.array)
        s = str.replace(s, '[', '(')
        s = str.replace(s, ']', ')')
        return str(s).replace(" ", "")

    def add(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        return [sum(x) for x in zip(self.array, other.array)]

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
b = Vector([3, 4, 5])

print(a.add(b))
print(a.array)
print(a.add(b))
