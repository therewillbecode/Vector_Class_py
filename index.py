__author__ = 'Tom'
import math


def calculate(a, b):
    return to_decimal(a) + to_decimal(b)


def to_decimal(a):
    a = [int(i) for i in list(a)]
    sum = 0
    j = len(a)-1
    for i in a:
        if i == 1:
            sum += math.pow(2, j)
        j -= 1
    return math.floor(sum)

