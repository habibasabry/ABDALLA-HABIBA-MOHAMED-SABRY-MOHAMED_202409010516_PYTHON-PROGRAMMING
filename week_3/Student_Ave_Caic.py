choice = "Y"

# Repeat the program while user chooses Y
while choice == "Y":

    # Get quiz marks from user
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    total = quiz_1 + quiz_2 + quiz_3
    average = total / 3

    # Calculate average mark
    print("Average =", average)

    # Check pass or fail
    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    # Ask user whether to continue
    choice = input("Continue? Select Y/N: ")

print("Program Ended")