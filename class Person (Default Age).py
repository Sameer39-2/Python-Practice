class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

Info = Person("Olly", 32)

Info.display()