# Import the function from food_order.py
from food_order import calculate_total


# Main function
def main():

    # Ask the user to enter the price
    price = float(input("Price (RM): "))

    # Ask the user to enter the quantity
    quantity = int(input("Quantity: "))

    # Calculate the total payment
    total = calculate_total(price, quantity)

    # Check whether the function returned an error message
    if isinstance(total, str):
        print(total)
    else:
        # Display the total payment with 2 decimal places
        print(f"Total Payment = RM {total:.2f}")


# Run the program
if __name__ == "__main__":
    main()

# Original buggy code
#print(f"Total Payment = RM {total:.2f}")