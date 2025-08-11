# Employee Management System (EMS)

# Step 1 - Initial Employee Data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Ridhima', 'age': 22, 'department': 'IT', 'salary': 60000},
    103: {'name': 'Aman', 'age': 30, 'department': 'Finance', 'salary': 55000}
}

# Step 3 - Add Employee Functionality
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Try a new one.")
            return
        
        name = input("Enter Employee Name: ").strip()
        age = int(input("Enter Employee Age: "))
        department = input("Enter Department: ").strip()
        salary = float(input("Enter Monthly Salary: "))
        
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print("✅ Employee added successfully!\n")
    except ValueError:
        print("Invalid input. Please enter the correct data type.\n")

# Step 4 - View All Employees
def view_employees():
    if not employees:
        print("No employees available.\n")
        return
    
    print("\n--- Employee List ---")
    print("{:<10} {:<15} {:<5} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(
            emp_id, details['name'], details['age'], details['department'], details['salary']
        ))
    print()

# Step 5 - Search for Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\n--- Employee Details for ID {emp_id} ---")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}\n")
        else:
            print("Employee not found.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

# Step 2 & Step 6 - Menu System
def main_menu():
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
