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

def write_employees(e_list):
    with open("employees.txt","a") as file:
        for e in e_list:
            file.write(str(e.to_dict()) + "\n")



def remove_employee(eid):
 # read data, find employee you want to delete , write the file
    employee_list = load_employees()
    for e in employee_list:
        if e.employee_id == eid:
            employee_list.remove(e)
            break
    write_employees(employee_list)

def update_employee(e_updated):
    employee_list = load_employees()
    for e in employee_list:
        if e.employee_id == e_updated.employee_id:
            e.salary = e_updated.salary
            break
    write_employees(employee_list)




















