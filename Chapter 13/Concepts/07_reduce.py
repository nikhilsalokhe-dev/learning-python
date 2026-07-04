from functools import reduce

num_list = [1, 2, 3, 4, 5]


def sum(a, b):
    return a + b


print(reduce(sum, num_list))
