## python-codechallenge2
# python-codechallenge2
 ## Yelp-style Domain Python Implementation

This Python implementation demonstrates a simplified Yelp-style domain with three main models: Restaurant, Customer, and Review. The code includes various methods to manage relationships, retrieve information, and perform aggregate operations within the domain.
Getting Started

To get started, ensure you have the required dependencies installed using the provided Pipfile.

bash

pipenv install

Classes and Instances
 ## Customer

    __init__(given_name, family_name): Initializes a new customer with a given name and family name.
    given_name(): Returns the customer's given name.
    family_name(): Returns the customer's family name.
    full_name(): Returns the full name of the customer.
    all(): Returns all customer instances.
    num_reviews(): Returns the total number of reviews authored by a customer.
    find_by_name(name): Class method to find a customer by their full name.
    find_all_by_given_name(name): Class method to find all customers with a given name.
    add_review(restaurant, rating): Adds a new review associated with the customer and a given restaurant.

## Restaurant

    __init__(name): Initializes a new restaurant with a name.
    name(): Returns the restaurant's name.
    all(): Returns all restaurant instances.
    reviews(): Returns a list of all reviews for a restaurant.
    customers(): Returns a unique list of customers who have reviewed a particular restaurant.
    average_star_rating(): Returns the average star rating for a restaurant based on its reviews.

## Review

    __init__(customer, restaurant, rating): Initializes a new review with a customer, restaurant, and rating.
    rating(): Returns the rating for a restaurant.
    all(): Returns all reviews.
    customer(): Returns the customer object for a review.
    restaurant(): Returns the restaurant object for a review.

Example Usage

python

# Create instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Great Food Place")
restaurant2 = Restaurant("Pizza Palace")

# Add reviews
review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

# Access information
print(customer1.full_name())  # Output: John Doe
print(restaurant1.average_star_rating())  # Output: 4.5
print(Customer.find_by_name("John Doe"))  # Output: <Customer object at ...>
print(Customer.find_all_by_given_name("John"))  # Output: [<Customer object at ...>]

## Author
Tasniim Yasin

