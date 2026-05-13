# if
# if else
# if elif else

def check_password_contains_alpha(password):
    # a - z ya A - Z
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for char in password:
        if char in alpha:
            count +=1

    if count < 2 or count > 5:
        return False
    return True

def check_password_contains_digit(password):
    number = '0123456789'
    for char in password:
        if char in number:
            return True
    return False

def check_password_contains_specialchar(password):
    special="@#!_&"
    count = 0

    for char in password:
        if char in special:
            count += 1

    if count >= 2 :
        return True
    return False

def check_password_contain_uppercase(password):
    uppercase = "ABCDEFGHIJKLMNOPQRST"
    count = 0
    for char in password:
        if char in uppercase :
            count +=1

    if count >= 5 :
        return False
    return True


def check_password_contain_lowercase(password):
    count = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in password:
        if char in alpha:
            count +=1
    if count >= 5 :
        return False
    return True


while True:
    password = input("Enter your password: ")

    # password show not be empty
    # password min len 6 & max len 12
    # password should contain at-least 1 char a-z Or A-Z
    # password should contain at-least 1 digit 0-9
    # password should contain special char (@,!,_,&,#)



    # Input: Mohit123
    if password == "":
        print("Password is empty")
    elif len(password) < 6 or len(password) > 12:
        print("Password should be between 6 and 12 characters")
    elif not check_password_contains_alpha(password):
        print("Password should contains at-least one character")
    elif not check_password_contains_digit(password):
        print("Password should contains at-least one digit")
    elif not check_password_contains_specialchar(password):
        print("Password should contain at least two special character (@,!,_,&,#)")
    elif not check_password_contain_uppercase():
        print("Password should contain atleast one uppercase character but it should be less than 5 characters")
    elif not check_password_contain_lowercase(password):
        print("Password should contain atleast one loweercase character but it should be less than 5 characters")
    else:
        print(f"Password: {password} is valid.")
        break

