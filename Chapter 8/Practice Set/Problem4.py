# 4. Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter a positive natural number: "))


def sum(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n + sum(n - 1)


print(f"The sum of first {n} natural numbers is: {sum(n)}")
