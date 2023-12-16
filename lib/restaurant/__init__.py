class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        print ("self.name")

    @classmethod
    def all(cls):
        print ("cls.all_restaurants")

    def reviews(self):
        print ("self.reviews")

    def customers(self):
        print ("list(set(review.customer() for review in self.reviews")

    def average_star_rating(self):
        if not self.reviews:
            print (0)
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)
