class Employee:

    def __init__(self, employee_id, name, department, designation, salary, experience, city):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary
        self.experience = experience
        self.city = city


    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "salary": self.salary,
            "experience": self.experience,
            "city": self.city
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["employee_id"],
                        data["name"],
                        data["department"],
                        data["designation"],
                        data["salary"],
                        data["experience"],
                        data["city"])

    def __str__(self):
        return (f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Designation: {self.designation},"
                f"Salary: {self.salary}, Experience: {self.experience}, City: {self.city}")

