# Student data
# (id, name, email, grade)

def save_student_to_file(s_id, name, email, grade):
    with open("student_record.txt", "a") as file:
        # 123,Mohit,mohit@gmail.com,9.5
        row = f"{s_id},{name},{email},{grade}\n"
        file.write(row)

def read_student_from_file():
    with open("student_record.txt", "r") as file:
        for row in file:
            s_id, name, email, grade = row.split(",") # [123, Mohit, mohit@gmail.com, 9.5]
            print(f"Id: {s_id} Name: {name} Email: {email} Grade: {grade}")


# save_student_to_file(1, "Mohit", "mohit@gmail.com", 9.6)
# save_student_to_file(2, "Karan", "karan@gmail.com", 7.6)
# save_student_to_file(3, "Aryan", "aryan@gmail.com", 8.9)

read_student_from_file()