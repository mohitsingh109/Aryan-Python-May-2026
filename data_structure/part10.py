#
# PROJECT: Student Course Registration System
#
# Imagine you are creating a small system for a college.
#
# The college wants to keep track of students and the courses they have enrolled in.
#
# Create a menu-driven Python program that allows a user to perform the following operations:
#
# 1. Add a new student.
# 2. Display all students.
# 3. Register a student for one or more courses.
# 4. View the courses registered by a student.
# 5. Remove a course from a student.
# 6. Find all students enrolled in a particular course.
# 7. Save all student data to a text file.
# 8. Load student data from a text file.
# 9. Exit the program.
#
# Available Courses:
# 1. Python Programming
# 2. Java Programming
# 3. Database Systems
# 4. Data Structures
# 5. Operating Systems
# 6. Cyber Security
# 7. Cloud Computing
#
# Requirements:
#
# - Every student must have a unique Student ID.
# - A student can register for multiple courses at the same time.
# - Course selection should be entered as comma-separated values.
#   Example:
#       1,3,5
#
# - Do not allow:
#     - Invalid course numbers
#     - Duplicate course selections
#     - Empty student names
#     - Duplicate Student IDs
#
# - Store student information in memory while the program is running.
#
# Example Menu:
#
# ===== STUDENT COURSE REGISTRATION SYSTEM =====
#
# 1. Add Student
# 2. View Students
# 3. Register Courses
# 4. View Student Courses
# 5. Remove Course
# 6. Search By Course
# 7. Exit
# """
student_info = {}
course_id = { "1" : "Python programming",
              "2":"Java Programming",
              "3":"Database system",
              "4":"Data structures",
              "5":"Operating systems",
              "6":"Cyber security",
              "7":"Cloud computing"}
course = {}

def add_student():
    global student_info
    name = str(input("Enter your name:"))
    s_id = int(input("Enter your id:"))
    year_enrollment = int(input("Enter your year enrollment:"))
    if s_id in student_info:
        print("Duplicate student id")
        return
    else:
        student_info[s_id] = {"name": name, "s_id" :s_id, "year_enrollment":year_enrollment}

def view_students():
    global student_info
    for record in student_info.values():
        print (f"Student ID: {record['s_id']},  Name : {record['name']}, Year Enrollment : {record['year_enrollment']}")

def register_course():
    global course_id, course , student_info
    s_id = input("Enter your id:")
    add_course = input("Enter your course number:")
    if s_id in student_info and add_course in course_id:
         if s_id in course:
             course[s_id].add(add_course)
         else:
             course[s_id] = {add_course}


def view_course():
    global course , student_info,course_id
    for s_id,c_ids in course.items():
        s_name = student_info[s_id]["name"]
        for c_id in c_ids:
            c_name = course_id[c_id]
            print(f" Student name : {s_name} and course:{c_name}")

def remove_course():
    global course, student_id , course_id
    for s_id, c_ids in course.items():
        s_name = student_info[s_id]["name"]
        for c_id in c_ids:
            c_delete = course_id[c_id]
            course.pop(c_delete)
            print(f"Student name : {s_name} and Course: {c_delete} removed")

def search_by_course():
    global course, student_id , course_id
    






while True:
    print("==========================")
    print("1.Add student")
    print("2.View students")
    print("3.Register courses")
    print("4.View student courses")
    print("5.Remove course")
    print("6.Search by  course")
    print("7.Exit")
    registration=input("Enter your choice:")
    if registration=="1":
        add_student()
    elif registration=="2":
        view_students()
    elif registration=="3":
        register_course()
    elif registration=="4":
        view_course()
    elif registration=="5":
        remove_course()
    elif registration=="6":

    elif registration=="7":
        print("exit")
        break
    else:
        print("Entered wrong choice")





