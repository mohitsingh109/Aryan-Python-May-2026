# 1. Class & Object
# What is class? ==> Form
# A class is a blueprint for creating object.
# student: id, name, marks, class_std, address...??

# Class (Form)
#  1. Constructor
#  2. instance variable
#  3. Function
class Student:

    # this is special function to init the value
    # self refer to current object
    # self use to init the object as well as to fetch the values from object
    # Constructor is the name of __init__
    def __init__(self, id, name, marks, address=None, email_id=None):
        self.id = id # Instance variable
        self.name = name # Instance variable
        self.marks = marks # Instance variable
        self.address = address # Instance variable
        self.email_id = email_id # Instance variable

    # Object function
    def display(self):
        print(f"Id: {self.id}, Name: {self.name}, Marks: {self.marks}, Address: {self.address}")


    def total_marks(self):
        return sum(self.marks)

# Object (Form fill by someone)
s_mohit = Student("STU_1", "Mohit", [10, 20, 30]) # by default call __init__ function
s_aryan = Student("STU_2", "Aryan", [47, 70, 40], "Canada")
#print(type(s_mohit))

s_mohit.display() # function of class
s_aryan.display()

print(s_mohit.total_marks())
print(s_aryan.total_marks())

# print(s_mohit.name) # Mohit
print(s_aryan.name)
# print(s_aryan.marks)
# print(s_aryan.address)
# print(s_mohit.address)


# a = int(10) # int class object
# print(type(a))
#
# b = str("hello")
# print(type(b))
#
# c = 4.5
# print(type(c))