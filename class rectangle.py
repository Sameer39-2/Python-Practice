class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return f" Area of Rectangle: {self.length * self.width}"
    def perimeter(self):
        return f" Perimeter of Rectangle: {2 * (self.length + self.width)}"
    
Rectangle = Rectangle(34,55)

print(Rectangle.area())
print(Rectangle.perimeter())
    