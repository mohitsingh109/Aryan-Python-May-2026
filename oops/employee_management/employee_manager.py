class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.employee_map = {} # Fast lookup


    def add_employee(self, e): # e = Employee class object
        if e.employee_id in self.employee_map:
            print("Employee already exists")
            return False

        self.employees.append(e)
        self.employee_map[e.employee_id] = e
        return True


    def remove_employee(self, eid):
        if eid not in self.employee_map:
            print("Employee does not exist")
            return False

        e = self.employee_map.pop(eid)
        self.employees.remove(e)
        return True


    def update_salary(self, eid, salary):
        if eid in self.employee_map:
            self.employee_map[eid].salary = salary
            return self.employee_map[eid]
        else:
            print("Employee does not exist")
            return None

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

    def search_by_salary_greater_than(self,salary):
        by_salary = []

        for e in self.employees:
            if e.salary >= salary:
                by_salary.append(e)

        return by_salary

    def search_by_experience_greater_than(self,experience):
        by_experience = []

        for e in self.employees:
            if e.experience >= experience:
                by_experience.append(e)

        return by_experience

    def group_by_department(self):
        by_department = {}

        for e in self.employees:
            if e.dapartment not in by_department:
                by_department[e.department] = [e]
            else:
                by_department[e.department].append(e)

        return by_department

    def highest_salary_employee(self):
        salary = None
        employee = None

        for e in self.employees:
            if e.salary > salary:
                salary = e.salary
                employee = e

        return employee

    def average_salary(self):
        total_salary = 0

        for e in self.employees:
            total_salary += e.salary

        return total_salary/len(self.employees)













