from oops.employee_management.employee import Employee

import ast
def save_employee(e):
    with open("employees.txt","a") as file:
        # file.write(f"{e.employee_id},{e.name},{e.department},{e.designation},{e.salary},{e.experience},{e.city}\n")
        file.write(str(e.to_dict()) + "\n")


def load_employees():
    employee_list = []
    with open("employees.txt","r") as file:
        for line in file:
            employee_dict = ast.literal_eval(line)
            e = Employee.from_dict(employee_dict)
            employee_list.append(e)
    return employee_list












