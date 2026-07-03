class Employee:
    salary = 1200000
    language = "Python"

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Hello User!")

    def __init__(self, name, salary, language):  # Dunder method (starts with __)
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")


harry = Employee(
    "Harry", 1300000, "JavaScript"
)  # Here this dunder method is called automatically.
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

# Here name is object attribute while salary & language are class attributes

harry.getInfo()
# This is the same as Employee.getInfo(Harry)

harry.greet()

"""
newName = Employee()  # This dunder method is called after an object is created(instantiated)
"""
