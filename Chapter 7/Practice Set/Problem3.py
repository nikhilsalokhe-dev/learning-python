# 3. Attempt problem 1 using while loop.

number = int(input("Enter a number: "))

i = 1
print(f"The multiplication table of {number} is: ")
while i < 11:
    print(f"{number} * {i} = {number * i}")
    i += 1
