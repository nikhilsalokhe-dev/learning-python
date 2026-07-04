a = 100  # Global variable
b = 2

print(f"Global b is {b}")


def fun():
    a = 1  # Local variable
    print(f"Local a is {a}")

    global b
    b = 22  # Now b is global


print(f"Global a is {a}")
fun()
print(f"Global b after updating is {b}")
