
# Function to get customer information
def get_customer():

    # Display heading
    print("=== Customer Information ===")

    # Get customer details from the user
    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")

    # Convert quantity into integer
    quantity = int(input("Quantity : "))

    # Convert price into float
    price = float(input("Price per Item (RM): "))

    # Ask whether delivery is needed
    delivery = input("Delivery (Y/N): ").upper()

    # Decide delivery charges using if-else
    if delivery == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00

    # Return all values back to main.py
    return name, food, quantity, price, delivery_charges
