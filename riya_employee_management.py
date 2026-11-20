
# Function to add a new employee
def add_employee(name, employee_id, salary):

    # Open the file in append mode to add new employee data
    with open("employees.txt", "a") as file:
        file.write(f"{name} | {employee_id} | {salary}\n")

    # Return a success message
    return "Employee Added Successfully"


# Function to view all employees
def view_employees():
    try:
        # Open the file in read mode
        with open("employees.txt", "r") as file:
            employees = file.readlines()

        # Check if the file is empty
        if len(employees) == 0:
            return "No employee records found."

        # Display all employee records
        print("\n--- Employee Records ---")

        for employee in employees:
            print(employee.strip())

        # Return a message after displaying the records
        return "All employee records displayed."

    except FileNotFoundError:
        # This message is shown if the file does not exist
        return "No employee records found."


# Main program
while True:

    # Display the main menu
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    # Take the user's choice
    choice = input("Choose Option: ")

    # Add employee option
    if choice == "1":
        name = input("Enter Name: ")
        employee_id = input("Enter ID: ")
        salary = input("Enter Salary: ")

        # Call the add_employee function
        message = add_employee(name, employee_id, salary)
        print(message)

    # View employees option
    elif choice == "2":

        # Call the view_employees function
        message = view_employees()
        print(message)

    # Exit option
    elif choice == "3":
        print("Program Exited.")
        break

    # Handle an invalid menu choice
    else:
        print("Invalid Option. Please try again.")