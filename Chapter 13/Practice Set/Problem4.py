# 4. Write a program to filter a list of numbers which are divisible by 5.


def divisible5(n):
    if n % 5 == 0:
        return True
    return False


a = [123, 3456, 123456, 345, 65, 15]

f = list(filter(divisible5, a))

print(f)
