import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f"Area: {math.pi * self.radius **2:.2f}" #To round the output to 2 decimal places,
        #we can format the floating-point numbers inside the f-string using :.2f.

 
    
    def circumference(self):
        return f"Circumference: {2 * math.pi * self.radius:.2f}"
    
Radius = Circle(34)

print(Radius.area())
print(Radius.circumference())
