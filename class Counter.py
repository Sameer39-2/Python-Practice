class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def display(self):
        print(f"Current Count: {self.count}")

Show = Counter()
Show.increment()   # count = 1
Show.decrement()   # count = 0
Show.reset()       # count = 0
Show.display()