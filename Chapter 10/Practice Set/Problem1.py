# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.


class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p1 = Programmer("Harry", 1200000, 234567)
print(
    f"{p1.name} is working at {p1.company} with salary of {p1.salary}$ who lives at pin code {p1.pin}."
)

p2 = Programmer("Nikhil", 1000000, 443210)
print(
    f"{p2.name} is working at {p2.company} with salary of {p2.salary}$ who lives at pin code {p2.pin}."
)
