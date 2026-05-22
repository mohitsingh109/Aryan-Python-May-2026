# Data structure
# 1. List
# 2. Tuple
# 3. Set
# 4. Dict


# 1. List
# - Order (it maintain the insertion order)
# - Mutable (edit/delete/add)
# - Allow duplicate
# - We can access element via a Index (start = 0, end < len(list) )
# - Negative index (Python only)

# empty list (recommended)
cart1 = []

# empty list: list()
# cart2 = list()

cart3 = ["Laptop", "Mouse"]
# print(cart3)

cart3.append("Keyboard")
# print(cart3)

cart3.remove("Mouse")
# print(cart3)

cart3.append("Wireless Mouse")
cart3.append("Pen drive")
# print(cart3)
#     -4          -3           -2               -1
#     0           1             2               3
# ['Laptop', 'Keyboard', 'Wireless Mouse', 'Pen drive']

# print(cart3[1])
# print(cart3[3])

# use to get the last element
# print(cart3[-1])
# print(cart3[-4])
cart3.append("key board")

# print(cart3)
cart3[-1] = "Keyboard" # edit operation
# print(cart3)

for product in cart3:
    print(product)