class Employee:  # Base Class
    company = "ITC"

    def show(self, name):
        self.name = name
        print(f"The name of employee is {self.name} and the company is {self.company}.")


class Programmer(Employee):  # Derived or child class
    company = "ITC InfoTech"

    def showLanguage(self, name, language):
        self.name = name
        self.language = language
        print(
            f"The name of programmer is {self.name} and he is good with {self.language} language."
        )


a = Employee()
b = Programmer()

b.show("Harry")
b.showLanguage("Harry", "Python")
