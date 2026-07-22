
# Import the function from ticket.py
from ticket import create_ticket

# Import the function from display.py
from display import display_ticket


def main():

    # store the returned values
    student_name, student_id, issue, location, priority = create_ticket()

    # Which technician should handle the ticket (priority level)
    if priority.lower() == "high":
        technician = "Ahmad"

    elif priority.lower() == "medium":
        technician = "Siti"

    else:
        technician = "Ali"

    # Ticket status
    status = "Pending"

    # Display the completed ticket
    display_ticket(
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician,
        status
    )


# Run the main function
if __name__ == "__main__":
    main()
