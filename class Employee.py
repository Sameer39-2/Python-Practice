class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self,amount):
        self.salary += amount
        print(f"Raise: {amount}, New Salary: {self.salary}")

    def display(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")


Emp1 = Employee("Alice", 34000)


Emp1.give_raise(10000)

Emp1.display()