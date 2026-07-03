class Employee:  # Parent / Base Class
    a = 1


class Programmer(Employee):  # Child Class 1 (of base class)
    b = 2


class Manager(Programmer):  # Child Class 2 (of child class 1)
    c = 3


o = Employee()
print(o.a)  # Prints only a attribute

o = Programmer()
print(o.a, o.b)  # Prints only a and b attributes

o = Manager()
print(o.a, o.b, o.c)  # Prints all a, b and c attributes
