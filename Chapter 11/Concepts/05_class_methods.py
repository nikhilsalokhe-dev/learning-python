class Employee:
    a = 1

    @classmethod  # Change in instance attributes won't change the attributes in the functions below this classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()

e.a = 45

e.show()
