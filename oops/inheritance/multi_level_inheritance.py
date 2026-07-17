"""
    Person
      |
    Employee
       |
    Developer
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age) # calling Person constructor
        self.employee_id = employee_id

class Developer(Employee):
    def __init__(self, name, age, employee_id, programming_language):
        super().__init__(name, age, employee_id) # calling Employee constructor
        self.programming_language = programming_language