class Employee:  # Parent / Base Class
    def __init__(self):
        print("Constructor of Employee")

    a = 1


class Programmer(Employee):  # Child Class 1 (of base class)
    def __init__(self):
        print("Constructor of Programmer")

    b = 2


class Manager(Programmer):  # Child Class 2 (of child class 1)
    def __init__(self):
        super().__init__()  # It will run the parent class (Programmer) too
        print("Constructor of Manager")

    c = 3


o = Manager()
print(o.a, o.b, o.c)
