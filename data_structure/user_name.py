users = []
passwords = []

def check_user_exists(user):
    global users

    for u in users:
        if u == user:
            return True
    return False

def add_user_to_list(username, password):
    global users
    global passwords

    if check_user_exists(username):
        print("\nUser already exists\n")
        return

    users.append(username)
    passwords.append(password)
    print(f"\nUser added: {username}\n")

def add_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    add_user_to_list(username, password)

def remove_user():
    global users
    username = input ("Enter your username:")
    if check_user_exists(username):
        users.remove(username)
        print(f"\n User removed: {username}\n")

def show_users():
    global users
    for u in users:
        print(u)




while True:
    print("=======================")
    print("Select an option:")
    print("1. Add user")
    print("2. Remove user")
    print("3. Show users")
    print("4. Exit")
    print("=======================")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_user()
    elif choice == 2:
        remove_user()
    elif choice == 3:
        show_users()
    elif choice == 4 :
        print("exit")
        break
    else:
        print("invalid choice")