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
    global course, student_info , course_id
    course_remove = input("Enter your course number :")
    for s_id, c_ids in course.items():
        s_name = student_info[s_id]["name"]
        if course_remove in c_ids:
            course[s_id].remove(course_remove)
            print(f"Student name : {s_name} and Course: {course_remove} removed")

def search_by_course():
    global course, student_info , course_id
    c_id = input("Enter your course number:")
    student_name = []
    for s_id, c_ids in course.items():
        if c_id in c_ids:
            c_name = course_id[c_id]
            s_name = student_info[s_id]["name"]
            print(f"Student name : {s_name}, Course: {c_name}")
            student_name.append(s_name)
    return  student_name

def search_by_year_enrollment(): #list , year of enrollment
    global student_info
    y_enrollment = int(input("Enter your year enrollment:"))
    result = []
    for record in student_info.values():
        if y_enrollment in record["year_enrollment"]:
            name = record["name"]
            s_id = record["s_id"]
            result.append(f"{name} - {s_id}")

def search_by_name(): # return all student with same name
    global student_info
    name = input("Enter your name:")
    result = []
    for record in student_info.values():
        if name == record["name"]:
            result.append(f"{name} : {record['s_id']}")
    return result


def search_by_course_name(): # print student info
    global course_id , course , student_info
    course_name = input("Enter your course name:")
    cu_id = None
    result = []
    for c_id,c_name in course_id.items():
        if c_name == course_name:
            cu_id = c_id
            break
    if not cu_id:
        return result
    for s_id,c_ids in course.items():
        if cu_id in c_ids:
            s_name = student_info[s_id]['name']
            s_year_enrollment = student_info[s_id]["year_enrollment"]
            result.append(f"{s_name} - {s_id} - {s_year_enrollment}")
    return result




while True:
    print("==========================")
    print("1.Add student")
    print("2.View students")
    print("3.Register courses")
    print("4.View student courses")
    print("5.Remove course")
    print("6.Search by  course")
    print("7. Search by year enrollment")
    print("8. search by name ")
    print("9. search by course name")
    print("10.Exit")
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
        search_by_course()
    elif registration=="7":
        search_by_year_enrollment()
    elif registration=="8":
        search_by_name()
    elif registration=="9":
        search_by_course_name()
    elif registration=="10":
        print("exit")
        break
    else:
        print("Entered wrong choice")





