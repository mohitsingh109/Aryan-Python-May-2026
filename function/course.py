# Course Management
# User can choose option
# 1. add a course
# 2. edit a course
# 3. delete a course (skip)
# 4. display a course
# 5. quit
#============#============#============#============#============#============#============#============
# infinite loop
# possible input (1, 2, 3, 4, 5)

# infinite loop here until user provide correct value
# 1. add a course
# id
# name
# description
# is_paid
# amount (if is_paid = true)

# validation ==> not empty for (id, name, description), amount should be > 0 if is_paid = true
# infinite loop here until user provide correct value
#============#============#============#============#============#============#============#============
# 2. edit a course
# name
# description
# is_paid
# amount (if is_paid = true)
# we'll update none empty value
#============#============#============#============#============#============#============#============

# add a course
    # while true
        # ==> input return 5 value
        # ==> validate
        # if validate pass break
        # else ask user again
c_id = None
name = None
description = None
paid = None
amount = None

def add_a_course():
    while True:
        global c_id, name, description, paid, amount
        c_id, name, description ,paid, amount = course_input ()
        state, message = validate_course_input()
        if state:
            display_course_details()
            break
        else :
            print(f"{message}")



def course_input():
    c_id = input("Enter a course id:")
    name = input("Enter a course name:")
    description = input("enter a course description :")
    paid = input("Enter a course is paid or free:")
    if paid == "paid":
        amount = int(input("enter a course amount:"))
    else:
        amount = 0
    return c_id, name, description, paid , amount

def display_course_details():
    global c_id, name, description, paid, amount
    print(f'Course id :{c_id}", name : {name}, desciption :{description}, paid :{paid}, amount : {amount}')

def validate_course_input():
    global c_id, name, description, paid, amount
    if len(c_id) > 6 or len(c_id) < 1:
        return False ,"Course id is too long or too short"
    if len(name) > 15 or len(name) < 5:
        return False ,"Course name is too long or too short "
    if len(description) > 15 or len(description) < 5 :
        return False, "Course description is too long or too short"
    if amount <= 0 and paid == "paid" :
        return False, "Course amount cannot be less than 0"
    return True, "Success"


def edit_course_details():
    global c_id, name, description, paid, amount
    c_id_edit,name_edit, description_edit, paid_edit, amount_edit = course_input()

    if c_id_edit != c_id or c_id is None:
        print("Course id does not match")
        return

    if c_id_edit != "" and c_id_edit is not None:
         c_id = c_id_edit

    if name_edit != "" and name_edit is not None:
        name = name_edit

    if description_edit != "" and description_edit is not None:
        description = description_edit

    if paid_edit != "" and paid_edit is not None:
        paid = paid_edit

    if amount_edit is not None and amount_edit == 0:
        amount = amount_edit

    display_course_details()

def delete_course():
    global c_id, name, description, paid, amount
    c_id_delete = input("Enter a course id to be deleted:")
    if c_id_delete != c_id:
        print("Course id does not match")
        return
    c_id = None
    name = None
    description = None
    paid = None
    amount = None









while True:
    print("\n------------------------------------------------------------\n")
    print("Course Management:")
    print("Please select and option:")
    print("1. Add new course")
    print("2. Edit a course")
    print("3. Delete a course")
    print("4. View a course")
    print("5. Quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_a_course()
    elif choice == 2:
        edit_course_details()
    elif choice == 3:
        delete_course()
    elif choice == 4:
        display_course_details()
    elif choice == 5:
        print("Quit")
        break
    else:
        print("Invalid choice")
