class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

    def display(self):
        print(f"{self.name} discount price: {self.price}")

x = Product("Burger", 100)
x.apply_discount(23)

x.display()