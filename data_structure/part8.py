

# change this to use dict

combination = {}

def add_build():
    global combination
    id = input("Enter id:")
    status = input("Enter status:")
    combination[id] = status
    print(f"{id} : {status}")


while True:
     print("1. Add  build status ")
     print("2. view build status by id")
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
