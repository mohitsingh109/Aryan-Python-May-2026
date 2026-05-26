# 3. Set
# - No Order
# - Mutable (edit/delete/add)
# - Not Allow duplicate
# - Unique Values
# - Fast to check if value exist
# - No Index (we cannot access element via a Index)
# - To perform lookup operation

# name1 = {}
# # name2 = set()
# names = {"Mohit", "Karan", "Aryan", "Aman"}
# names.remove("Mohit")
# #
# for name in names:
#     print(name)
#
# names.add("Rohit")
# names.add("Mohit")
#
# for name in names:
#     print(name)
#
# # Hash table
# print("Mohit" in names) # O(1)
#
# # print(names[0])

user_name = ["Karan", "Aman", "Aryan"] # to store order data
look_up_set = set(user_name) # to look up fast
while True:
    print(user_name)
    name = input("Enter your name: ")
    if name == "end":
        break

    if name not in look_up_set: # O(1) Fast
        user_name.append(name)
        look_up_set.add(name)
        print("User " + name + " is added")
    else:
        print("User " + name + " is already added")


