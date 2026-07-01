# Tutorial 5 Documentation :)

# 1.1 Problem Statement

Develop a Python program for a small café that automatically calculates a customer's total bill based on the quantity of coffee, tea, and sandwiches ordered. The program should also display a receipt.

---

## 1.2 Inputs

- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity

---

## 1.3 Outputs

- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity
- Total bill (RM)

---

## 1.4 Typical Process Flow

1. Ask the customer for their name.
2. Ask for the quantity of coffee.
3. Ask for the quantity of tea.
4. Ask for the quantity of sandwiches.
5. Calculate the total cost.
6. Display the receipt.
7. Display the total amount to pay.

---

## 1.5 Constraints

- Coffee price = RM8.50
- Tea price = RM6.00
- Sandwich price = RM12.00
- Quantities should be zero or positive integers.

---

# 2. Problem Decomposition

The program can be divided into the following smaller tasks:

1. Get customer information.
2. Get quantities for each menu item.
3. Calculate the total bill.
4. Print the receipt.
5. End the program.

---

# 3. Pseudocode

START

Display welcome message

Input customer name

Input coffee quantity

Input tea quantity

Input sandwich quantity

Calculate total
    total = (coffee × 8.50) +
            (tea × 6.00) +
            (sandwich × 12.00)

Display receipt

Display customer name

Display coffee quantity

Display tea quantity

Display sandwich quantity

Display total bill

END
