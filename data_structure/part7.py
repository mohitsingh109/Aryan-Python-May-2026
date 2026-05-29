# Dict

# 1. Dict
# - Order (it maintain the insertion order yes but by key)
# - Mutable (edit/delete/add) Yes
# - Allow duplicate
#     - No: Key
#     - Yes: Value
# - No Index
# - It's a Key value pair

# student_data = {
#     "101": "Mohit",
#     "102": "Aryan",
#     "103": "Aman"
# }
#
# for k, v in student_data.items():
#     print(k, v)
#
# print(student_data["103"])
#
# student_data["103"] = "Rohit" # edit operation
# print(student_data)
#
# student_data.pop("102") # delete operation
# print(student_data)
#
# student_data["104"] = "Gagan" # add operation
# print(student_data)

# Cart (username, email, product_count, amount, product)

amazon_cart = {
    "101": {
        "username": "Mohit",
        "email": "mohit@gmail.com",
        "product_count": 3,
        "amount": 10,
        "products": ["I-Phone", "Gift"]
    },
    "102": {
        "username": "Aryan",
        "email": "aryan@gmail.com",
        "product_count": 2,
        "amount": 20,
        "products": ["MacBook", "Shirt", "Gift"]
    }
}

print(amazon_cart["101"]["email"])
print(amazon_cart["102"]["amount"])

# I want to print all username
print("========================")
for value in amazon_cart.values():
    print(value["username"])

print("========================")
for key in amazon_cart.keys():
    print(key)

if "101" in amazon_cart:
    print("101 is present in cart")

if "104" not in amazon_cart:
    print("104 is not present in cart")

# I want to add a new product in Aryan cart
products = amazon_cart["102"]["products"]
print(products)

if "Gift" not in products:
    print("Gift is not present in cart")
    products.append("Gift")

print(amazon_cart["102"])