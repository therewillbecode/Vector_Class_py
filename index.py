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

    def equals(self, other):
        return self.__dict__ == other.__dict__

    def add(self, other):
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        self.array = [sum(x) for x in zip(self.array, other.array)]
        return self

    def subtract(self, other):
        print(self)
        print(other)
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        c = [(x1 - x2) for (x1, x2) in zip(self.array, other.array)]
        return Vector(c)

    def dot(self, other):
        print(self)
        print(other)
        if self.length != other.length:
            raise AttributeError("Vector length not equal")
        dot = sum([(x1 * x2) for (x1, x2) in zip(self.array, other.array)])
        return dot

    def norm(self):
        nor = math.sqrt(sum([math.pow(x, 2) for x in self.array]))
        return nor
a = Vector([4, 6, 8])
b = Vector([3, 4, 5])

print('i')
print(a.dot(b))
print(a.subtract(b).equals(Vector([1,2,3])))

