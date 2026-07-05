def add_employee():
    global employee
    id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    designation = input("Enter designation: ")
    salary = int(input("Enter salary: "))
    experience = int(input("Enter experience: "))
    city = input("Enter city: ")
    for id, values in employee.items():
        if id != id:
            employee[id] = {"id" = id , "name" = name,"department" = department, "designation" = designation, "salary" = salary, "experience" = experience, "city" = city}

        else:
            print(f"Employee with id {id} already exists")


def remove_employee():
    global employee
    e_id = int(input("Enter employee id: "))
    for id, values in employee.items():
        if id == id:
            employee[id].remove(e_id)


def update_salary():
    global employee
    id = int(input("Enter employee id: "))
    for id, values in employee.items():
