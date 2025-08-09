class Animal:
    def make_sound(self):
        print("Make sound.")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

A= Animal()
A.make_sound()

D = Dog()
D.make_sound()
