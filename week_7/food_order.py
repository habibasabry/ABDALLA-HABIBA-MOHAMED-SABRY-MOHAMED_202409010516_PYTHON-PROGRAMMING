# Function to calculate the total payment
def calculate_total(price, quantity):

    # Check if the price is negative
    if price < 0:
        return "invalid price"

    # Check if the quantity is negative
    if quantity < 0:
        return "invalid quantity"

    # Return the total price
    return price * quantity