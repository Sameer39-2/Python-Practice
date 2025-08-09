class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return f"{self.celsius} C in Fahrenheit: {(self.celsius * 9 / 5) + 32:.2f}"
    
    def to_kelvin(self):
        return f"{self.celsius} C in Kelvin: {self.celsius + 273.15:.2f}"
    

Convert = Temperature(23.12)

print(Convert.to_fahrenheit())
print(Convert.to_kelvin())