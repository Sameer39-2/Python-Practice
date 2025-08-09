class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_hit(self):
        if self.rating > 8.0:
            return True
        else:
            return False

Details = Movie("Superman", "James Gunn", 8.9)

print(Details.is_hit())