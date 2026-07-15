
# Import function from customer module
from customer import get_customer

# Import function from receipt module
from receipt import print_receipt


# Main function
def main():

    # Get all customer information
    name, food, quantity, price, delivery_charges = get_customer()

    # Print the receipt
    print_receipt(name, food, quantity, price, delivery_charges)


# Run the program
if __name__ == "__main__":
    main()
