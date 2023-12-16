# main.py
# Example usage and testing of the classes and methods

# Import your classes
from customer import Customer
from restaurant import Restaurant
from review import Review

# Create instances and test your code
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Great Food Place")
restaurant2 = Restaurant("Pizza Palace")

review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

# Access information
print(customer1.full_name())  # Output: John Doe
print(restaurant1.average_star_rating())  # Output: 4.5
print(Customer.find_by_name("John Doe"))  # Output: <Customer object at ...>
print(Customer.find_all_by_given_name("John"))  # Output: [<Customer object at ...>]
