# Import the function to be tested
from food_order import calculate_total


# Test normal calculation
def test_order1():
    assert calculate_total(10, 2) == 20


# Test another valid calculation
def test_order2():
    assert calculate_total(5, 2) == 10


# Test when quantity is zero
def test_order3():
    assert calculate_total(5, 0) == 0


# Test invalid price
def test_order4():
    assert calculate_total(-5, 2) == "invalid price"


# Test invalid quantity
def test_order5():
    assert calculate_total(10, -2) == "invalid quantity"
