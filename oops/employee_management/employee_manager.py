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

        e = self.employee_map.pop(eid)
        self.employees.remove(e)


    def update_salary(self, eid, salary):
        if eid in self.employee_map:
            self.employee_map[eid].salary = salary
        else:
            print("Employee does not exist")

    def search_by_id(self, eid):
        if eid in self.employee_map:
            return self.employee_map[eid]
        else:
            print("Employee does not exist")
            return None

    def search_by_department(self, department):
        result = []

        for e in self.employees:
            if e.department == department:
                result.append(e)

        return result

    def search_by_city(self,city):
        by_city = []

        for e in self.employees:
            if e.city == city:
                by_city.append(e)

        return by_city


