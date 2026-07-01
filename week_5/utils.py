# Function to calculate the total customer bill
def calculate_total(coffee, tea, sandwich):
    # Calculate the total price based on the menu prices
    total = (coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)

    # Return the total amount
    return total


# Function to print the customer receipt
def print_receipt(customer, coffee, tea, sandwich, total):
    # Display receipt heading
    print("===== RECEIPT =====")

    # Display customer information
    print("Customer :", customer)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)

    # Display separator line
    print("-------------------")

    # Display the total bill with 2 decimal places
    print(f"Total = RM {total:.2f}")