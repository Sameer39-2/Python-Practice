class Calculator:

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def substract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def division(self):
        if self.b == 0 :
            return "Error! Cannot divide by zero."
        else:
            return f"{self.a / self.b :.2f}"

Start = Calculator(23,43)

print("Addition: " ,Start.add())
print("Substraction: ", Start.substract())
print("Multiply: ", Start.multiply())
print("Division: ", Start.division())