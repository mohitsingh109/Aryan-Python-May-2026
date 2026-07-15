# Inheritance
# It allows to remove duplicate code by moving it to the parent class and child class
# can use it by inheriting the parent class

# Inheritance Type:
# Single Inheritance (No) (Parent --> Child)
# Multi level Inheritance (No): (Grand Parent -> Parent -> Child)
# Hierarchy Inheritance (Yes) (Parent --> C1)
#                              |--> C2
# Hybrid (Yes)

# Parent class / Super class
class Employee:
    def __init__(self, emp_id, name, email, address, salary):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary

    def display(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Address:",self.address)
        print("Salary:",self.salary)

# Child class / Sub class
class Manager(Employee): # Employee is parent class and Manager is child class
    def __init__(self, emp_id, name, email, address, salary, team_size):
        # parent constructor
        # super() - it represent the parent class and we can call the parent class constructor
        super().__init__(emp_id, name, email, address, salary) # it should always be the first line in the constructor of child class
        self.team_size = team_size

    def conduct_meeting(self):
        print("Conducting meeting with the team of size:", self.team_size)


class Developer(Employee):
    def __init__(self, emp_id, name, email, address, salary, programming_language):
        super().__init__(emp_id, name, email, address, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"Writing code in {self.programming_language}")



m1 = Manager(1, "Aryan", "aryan@gmail.com", "123 Main School", 500, 10)
print(m1.team_size)
print(m1.salary) # ?? yes
print(m1.address)
m1.conduct_meeting()
m1.display()

print("================================")
d1 = Developer(1, "Mohit", "msingh@gmail.com", "123 Main School", 3000, "Python")
d1.write_code()
d1.display()
