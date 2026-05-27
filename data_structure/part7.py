# Dict

# 1. Dict
# - Order (it maintain the insertion order yes but by key)
# - Mutable (edit/delete/add) Yes
# - Allow duplicate
#     - No: Key
#     - Yes: Value
# - No Index
# - It's a Key value pair

student_data = {
    "101": "Mohit",
    "102": "Aryan",
    "103": "Aman"
}

for k, v in student_data.items():
    print(k, v)

print(student_data["103"])

student_data["103"] = "Rohit" # edit operation
print(student_data)

student_data.pop("102") # delete operation
print(student_data)

student_data["104"] = "Gagan" # add operation
print(student_data)