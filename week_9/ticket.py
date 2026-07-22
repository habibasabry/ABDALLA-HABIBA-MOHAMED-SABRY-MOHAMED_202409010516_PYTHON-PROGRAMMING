
def create_ticket():

    print("=== IT Helpdesk Ticket ===")

    # Get user details for the ticket 
    student_name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")

    # Ask the user to choose the priority
    priority = input("Priority (High/Medium/Low): ")

    # Return all values back to main.py
    return student_name, student_id, issue, location, priority
