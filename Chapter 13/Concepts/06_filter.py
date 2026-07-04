num_list = [1, 2, 3, 4, 5]


def even(n):
    if n % 2 == 0:
        return True
    return False


onlyEven = filter(even, num_list)

print(list(onlyEven))
