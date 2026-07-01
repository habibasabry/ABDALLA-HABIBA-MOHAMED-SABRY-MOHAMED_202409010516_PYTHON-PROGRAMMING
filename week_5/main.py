# Import the functions from utils.py
from utils import calculate_total, print_receipt

# Ask the customer for their name
customer = input("Customer name: ")

# Ask for the quantity of each item
coffee = int(input("Coffee quantity: "))
tea = int(input("Tea quantity: "))
sandwich = int(input("Sandwich quantity: "))

# Calculate the total bill
total = calculate_total(coffee, tea, sandwich)

# Print the customer receipt
print_receipt(customer, coffee, tea, sandwich, total)