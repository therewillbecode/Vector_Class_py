__author__ = 'Tom'
import math

class Vector:
    def __init__(self, arr):
        self.array = arr
        self.length = len(arr)

    def __repr__(self):
        return self.array

    def __str__(self):
        s = str(self.array)
        s = str.replace(s, '[', '(')
        s = str.replace(s, ']', ')')
        return str(s).replace(" ", "")

    def equals(self, other):
        return self.array == other.array

    def add(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        self.array = [sum(x) for x in zip(self.array, other.array)]
        print(Vector(self.array))
        return Vector(self.array)

    def subtract(self, other):
 #       print(self)
  #      print(other)
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        self.array = [(x1 - x2) for (x1, x2) in zip(self.array, other.array)]
        b = Vector(self.array)
#        print(b)
        return b

    def dot(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        self.array = sum([(x1 * x2) for (x1, x2) in zip(self.array, other.array)])

    def norm(self):
        self.array = math.sqrt(sum([math.pow(x, 2) for x in self.array]))


a = Vector([4, 6, 8])
b = Vector([3, 4, 5])

print(a.subtract(b))
print(a.array)
print(a)

