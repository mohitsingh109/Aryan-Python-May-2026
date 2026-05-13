# def <name> (arguments...)

def add(value1, value2): # I've define my function
    result = value1 + value2
    print(result)

# a = 10
# b = 20
# c = a + b
# print(c)
add(10, 20) # we are calling a function
add(34, 56)
# e = 34
# h = 56
# f = e + h
# print(f)

# Function with no argument & no return value
def greeting():
    print("hello world")
    # return None

# Function with one argument & one return value
def welcome(name): #name="Michael"
    result = f"hello {name}"
    return result

# Function with multiple argument and one with default value & one return value
def account(name, phone=None, amount = 0):
    account_summary = f"account {name} has {phone} with {amount}"
    return account_summary

# Function with multiple value in return type
def stock_details():
    return "AAPL", "Apple Inc.", "NASDAQ"

# greeting()
# blabla = "Michael"
# message = welcome(blabla) # welcome("Michael")
# print(message)
# user_name = input("Enter your name: ")
# mobile = input("Enter your phone number: ")
# s1 = account(user_name, mobile)
# # s2 = account('Aryan', '7888770232', 10)
# print(s1)
# print(s2)

# ticket, stock_name, exchange = stock_details()
# print(ticket)
# print(stock_name)
# print(exchange)
#
# _, stock_name, _ = stock_details()
# print(stock_name)

# result = greeting()
# print(result)#.... None