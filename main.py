from employee import add_employee
from attendance import mark_attendance
from leave import apply_leave
from salary import show_salary
from performance import update_performance

file_path = 'database.csv'


# ✅ Wrapper to collect user input and call the new add_employee() correctly
def add_employee_console(file_path):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    try:
        add_employee(file_path, emp_id, name, age, dept, salary)
        print("✅ Employee added successfully.")
    except Exception as e:
        print(f"❌ Error adding employee: {e}")


def main():
    while True:
        print("\n===== HR Management Assistant =====")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. Apply Leave")
        print("4. Show Salary")
        print("5. Update Performance")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee_console(file_path)
        elif choice == '2':
            mark_attendance(file_path)
        elif choice == '3':
            apply_leave(file_path)
        elif choice == '4':
            show_salary(file_path)
        elif choice == '5':
            update_performance(file_path)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
