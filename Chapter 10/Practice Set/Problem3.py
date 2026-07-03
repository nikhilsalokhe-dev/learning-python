# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.
# Does this change the class attribute?


class Demo:
    a = 4


object = Demo()
print(
    f"The value of a is {object.a}."
)  # Prints the class attribute (as there is no instance attribute)

object.a = 0  # Instance attribute is set.
print(f"The updated value of a is {object.a}.")  # Prints the instance attribute

print(Demo.a)  # Prints the class attribute

"""
Final Answer: Class Attribute does not change.
"""
