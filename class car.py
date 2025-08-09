class Car:
    def __init__(self, brand, models, year):
        self.brand = brand
        self.models = models
        self.year = year

    def start(self):
        print("Car started")

    def info(self):
        print(f"Brand: {self.brand}, Models: {self.models}, Year: {self.year}")

my_car = Car("Tesla", "A64", 2020)

my_car.info()
my_car.start()