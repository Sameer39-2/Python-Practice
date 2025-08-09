class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return f"{self.title} by {self.author} , {self.year}"
    

Summary = Book("IT", "Stephen King", 1986)

print(Summary.get_summary())