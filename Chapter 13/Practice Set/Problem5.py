# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

a = [12, 53, 16, 765, 123, 752]


def maximum(x, y):
    if x > y:
        return x
    return y


greatest = reduce(maximum, a)

print(greatest)
