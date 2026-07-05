class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.employee_map = {} # Fast lookup


    def add_employee(self, e): # e = Employee class object
        if e.employee_id in self.employee_map:
            print("Employee already exists")
            return

        self.employees.append(e)
        self.employee_map[e.employee_id] = e


    def remove_employee(self, eid):
        if eid not in self.employee_map:
            print("Employee does not exist")
            return

        self.employee_map.pop(eid) # dict remove??
        # ---- ?
        # Do i have index of eid in employee list?
        # No

        # Do i have value to remove it from employee list?
        # No
        for e in self.employees:
            if e.employee_id == eid:
                self.employees.remove(e)
                break


    def update_salary(self, eid, salary):
        pass


    def search_by_id(self, eid):
        pass

