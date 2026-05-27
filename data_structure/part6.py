# High level input option 1. to add a build stats, 2 to view build stats 3. quit

# PASSED, FAILED, RUNNING, SKIP, QUEUED, ERROR

# input
# build id
# build status

# build id + stats (unique combination)
# Order data

# build id: 1
# build status: QUEUED

# build id: 1
# build status: RUNNING

# Can you tell me order status for build id 1
# [QUEUED, RUNNING]

# build id: 1
# build status: RUNNING

# build id: 1
# build status: PASSED

# Can you tell me order status for build id 1
# [QUEUED, RUNNING, PASSED]

# Can you tell me order status for build id 2
# []

combination = []
status_check = set()

def input_build_info():
    id = input("Enter id :")
    status = input ("Enter status:")
    return id, status

def add_build():
    id , status = input_build_info()
    global combination , status_check
    combine = id +":"+ status

    if combine not in status_check:
        status_check.add(combine)
        combination.append(combine)

def view_build():
    global combination
    print(f"{combination}")

def view_build_by_id():
    global combination
    id = input("Enter id:") + ":"
    for item in combination:
       if  item.startswith(id):
        print(f" {item} ")








while True:
     print("1. Add  build status ")
     print("2.view build status by id")
     print("3. View all build")
     print("4. exit")
     choice = input("Enter your choice:")
     if choice == "1":
         add_build()
     elif choice == "2":
         view_build_by_id()
     elif choice == "3":
         view_build()
     elif choice == "4":
         break
     else:
         print("Invalid choice")
