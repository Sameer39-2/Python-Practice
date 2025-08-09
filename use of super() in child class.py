class Animal:
    def __init__(self, name):
        self.fname = name
        print(f"{self.fname} is an animal.")

class Dog(Animal):
    def __init__(self, fname, breed):
        super().__init__(fname) #class the parent counstructor
        self.breed = breed
        print(f"{self.fname} is  {self.breed}")

D = Dog("Tom", "Dogesh bhai")

