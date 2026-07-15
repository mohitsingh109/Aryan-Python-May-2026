# emp_id, name, email, salary, team_size

class Manager:
    def __init__(self, emp_id, name, email, address, salary, team_size):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary
        self.team_size = team_size


    def display(self):
        print(self.name)
        print(self.email)
        print(self.address)
        print(self.salary)


# Developer
# emp_id, name, email, salary, programming_language
class Developer:
    def __init__(self, emp_id, name, email, address, salary, programming_language):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary
        self.programming_language = programming_language

    def display(self):
        print(self.name)
        print(self.email)
        print(self.address)
        print(self.salary)


# Inheritance
# It allows to remove duplicate code by moving it to the parent class and child class can use it by inheriting the parent class
