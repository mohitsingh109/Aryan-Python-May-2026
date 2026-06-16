# file = open("student.txt", "r")
# data = file.read()
# print(data)
# # calculation (issue occur)
# file.close()

# Problem in above code?
# - if an error occur before file close it remain open

# Use with keyword
# Auto close the file after the end block
# file = open("student.txt", "r")
with open("student.txt", "r") as file:
    data = file.read()
    print(data)