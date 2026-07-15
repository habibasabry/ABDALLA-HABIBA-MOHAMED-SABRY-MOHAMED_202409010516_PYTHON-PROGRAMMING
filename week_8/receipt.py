
# Function to print the receipt
def print_receipt(name, food, quantity, price, delivery_charges):

    # Calculate subtotal
    subtotal = quantity * price

    # Calculate 5% service charge
    service_charge = subtotal * 0.05

    # Calculate grand total
    grand_total = subtotal + service_charge + delivery_charges

    # Print receipt heading
    print("\n========== RECEIPT ==========")

    # Print customer details
    print(f"Customer : {name}")
    print(f"Food     : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price    : RM {price:.2f}")

    print("--------------------------------")

    # Print payment details
    print(f"Subtotal : RM {subtotal:.2f}")
    print(f"Service Charge (5%) : RM {service_charge:.2f}")
    print(f"Delivery Charge : RM {delivery_charges:.2f}")

    print("--------------------------------")

    # Print final amount
    print(f"TOTAL : RM {grand_total:.2f}")

    print("==============================")
