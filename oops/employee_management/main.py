from oops.employee_management.employee import Employee
from oops.employee_management.employee_manager import EmployeeManager
from oops.employee_management.employee_storage import save_employee, load_employees


def display_option():
    print("""
    1. Add Employee
    2. Remove Employee
    3. Update Salary
    4. Search by ID
    5. Search by Department
    6. Search by City
    7. Salary Report
    8. Experience Report
    9. Save to File
    10. Load from File
    11. Exit
    """)

def create_employee():
    e_id = input("Enter employee id: ")
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    designation = input("Enter designation: ")
    salary = int(input("Enter salary: "))
    experience = int(input("Enter experience: "))
    city = input("Enter city: ")
    return Employee(e_id, name, department, designation, salary, experience, city)

def load_all_employees(em):
    employee_list = load_employees()
    for e in employee_list:
        em.add_employee(e)

employee_manager = EmployeeManager()
load_all_employees(employee_manager)

while True:
    display_option()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        e = create_employee() # taking input from user to create employee object
        employee_manager.add_employee(e) # it stores it into list & dict
        save_employee(e)
    else:
        break


