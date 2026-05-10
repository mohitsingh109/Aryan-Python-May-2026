# loops --> for , while


# for <var> in <itr>
# 0 -- 99
# range(100) ==> start = 0; end < 100; step = 1
# for i in range(100):
#     print(i)
#
# print("==============")
# 1 to 100
# range(1, 101) ==> start = 1; end < 101; step = 2
# for i in range(1, 101, 2):
#     print(i)

# 100 to 1
# print("==============")
# for i in range(100, 0, -1):
#     print(i)

# for (list of amazon cart order total price)
# for (list of video to show in YouTube when someone search Python)

# While
# player = True
#
# while player:
#     print("Player is on")
#     state = input("Enter player state")
#     if state == "quit":
#         player = False

# start = 1
#
# while start <= 100:
#     print(start)
#     start += 1 # 1-->2-->3

# break & continue
# 0 - 9
# num = int(input("Enter a number: "))
# for i in range(10):
#     if num == i:
#         break
#     print(i)
# num = int(input("Enter a number: "))
# for i in range(10):
#     if num == i:
#         continue
#     print(i)

# name = input("Please enter your name: ") # Azar
# # for <var> in <itr>
# for char in name:
#     if char == 'z' or char == 'Z':
#         print(f"{name} contains z")

# password contains any char from a - z, A - Z?

password = '@1#Abc#'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# for char in password:
#     if char in alphabet:
#         print(f"{password} is valid and contains alphabet")
#         break

# for i in range(10):
#     if str(i) in password:
#         print(f"Password: {password} is valid & contain 0-9")
#         break