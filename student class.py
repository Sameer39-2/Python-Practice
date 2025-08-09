class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    def display(self):
        print(f"Student name is {self.name} with roll number : {self.roll_number}")


student1 = Student("Sameer", 37)

student1.display()