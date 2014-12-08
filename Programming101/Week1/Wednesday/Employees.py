class Employee():

    def __init__(self, givenName, familyName):
        self.givenName = givenName
        self.familyName = familyName


class HourlyEmployee(Employee):

    def __init__(self, givenName, familyName, workHours):
        super().__init__(givenName, familyName)
        self.workHours = workHours

    def calculateCash(self, money):
        return self.workHours * money


class SalaryEmployee(Employee):

    def __init__(self, givenName, familyName, annualSalary):
        super().__init__(givenName, familyName)
        self.annualSalary = annualSalary

    def calculateCash(self):
        return self.annualSalary


class Manager(SalaryEmployee):

    def __init__(self, givenName, familyName, annualSalary, bonus):
        super().__init__(givenName, familyName, annualSalary)
        self.bonus = bonus

    def calculateCash(self):
        return self.annualSalary + self.bonus


hourly_emp = HourlyEmployee("Svetlin", "Slavov", 40)
salary = SalaryEmployee("Ivan", "Ivanov", 1000)
manager = Manager("Spinder", "Man", 3000, 450)
print (hourly_emp.calculateCash(3))
print (salary.calculateCash())
print (manager.calculateCash())
