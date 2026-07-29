# Exception is a mechanism to catch errors in Python.
# It allows you to handle exceptions gracefully instead of crashing the program.

# num = int(input("Enter a number: "))
# result = 100 / num
# print(result)

# try & except
# try block contains code that may cause an exception

# List of exception
"""
ZeroDivisionError  --> Division by zero
ValueError  --> Type casting/Invalid input/operation
TypeError  --> Wrong data type
IndexError  --> Index out of range
KeyError  --> Key not found in dictionary
FileNotFoundError  --> File not found
"""

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please enter a valid number.")


# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(result)
# except Exception as e: # 99.99%
#     print("Something went wrong.")
#     print(e)

# Else block (Very rare)
# else block run if no exception occurs in try block
# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Result=",result)


# finally block always run whether exception occurs or not
# for doing cleanup operation

# SBI login
# password == db_password (mismatch)
# db connection ---> I need to release this resource
# sms connection SMTP --> I need to release this also
# debugging --> send a sms (pass/fail)

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Release db connection")
    print("Release db sms SMTP connection")
