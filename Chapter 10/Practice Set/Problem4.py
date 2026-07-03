# 4. Add a static method in problem 2, to greet the user with hello.

n = int(input("Enter a number: "))


class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}.")

    def cube(self):
        print(f"The cube of {self.n} is {self.n * self.n * self.n}.")

    def square_root(self):
        print(f"The square root of {self.n} is {round(self.n ** (1 / 2), 2)}.")

    @staticmethod
    def greet():
        print("Hello There!")


a = Calculator(n)

a.greet()
a.square()
a.cube()
a.square_root()
