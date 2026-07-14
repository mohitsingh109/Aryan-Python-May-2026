from oops.employee_management.employee import Employee
from oops.employee_management.employee_manager import EmployeeManager
from oops.employee_management.employee_storage import save_employee, load_employees , remove_employee , update_employee


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
    9. Exit
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

def display_employees(e_list):
    for e in e_list:
        print(e)


employee_manager = EmployeeManager()
load_all_employees(employee_manager)

while True:
    display_option()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        e = create_employee()# taking input from user to create employee object
        is_add_employee = employee_manager.add_employee(e)
        if is_add_employee:
            save_employee(e)
    elif choice == 2:
        eid = input("Enter employee id: ")
        is_deleted = employee_manager.remove_employee(eid)
        if is_deleted:
            remove_employee(eid)
    elif choice == 3:
        eid = input("Enter employee id: ")
        salary = int(input("Enter salary: "))
        updated_e = employee_manager.update_salary(eid, salary)
        if updated_e:
            update_employee(updated_e)
    elif choice == 4:
        eid = input("Enter employee id: ")
        search_e = employee_manager.search_by_id(eid)
        if search_e:
            print(search_e)
    elif choice == 5:
        department = input("Enter department: ")
        e_list = employee_manager.search_by_department(department)
        display_employees(e_list)
    elif choice == 6:
        city = input("Enter city: ")
        e_list = employee_manager.search_by_city(city)
        display_employees(e_list)
    elif choice == 7:
        salary = int(input("Enter salary: "))
        e_list = employee_manager.search_by_salary_greater_than(salary)
        display_employees(e_list)
    elif choice == 8:
        experience = int(input("Enter experience: "))
        e_list = employee_manager.search_by_experience_greater_than(experience)
        display_employees(e_list)
    elif choice == 9:
        break
    else:
        print("Invalid choice")



