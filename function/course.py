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
#============#============#============#============#============#============#============#============
# infinite loop here until user provide correct value
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
        print("Add new course") # you will call a function
    elif choice == 2:
        print("Edit a course")
    elif choice == 3:
        print("Delete a course")
    elif choice == 4:
        print("View a course")
    elif choice == 5:
        print("Quit")
        break
    else:
        print("Invalid choice")
