# # Local / Global variable
#
# val = 40 # global variable
# print(val) # 40
# def f1():
#     global val
#     val = 10 # local variable
#     print(val) # 10
#     val = val + 1
#     print(val) # 11
#
# print(val) # 40
# f1()
# print(val) # 11



#
# def f1(a):
#     a = a + 5
#     print("f1", a) # f1 11
#
# def f2():
#     a = 5
#     print("f2",a) # f2 5
#
# def f3():
#     global a
#     a = a - 4
#     print("f3",a) # f3 6
#
# a = 10
#
# f3()
# print("outside-1",a) # outside-1 6
# f1(a)
# print("outside-2",a) # outside-2 6
# f2()
# print("outside-3",a) # outside-3 6

# Result:f3 6, outside-1 6, f1 15, outside-2 15, f2 5, outside-3 5


# def abc(a, b, c):
#     print("abc", a, b, c) # 11, 12, 10
#     a = a + 2
#     b = b + 3
#     c = c + 4
#     print(a, b, c) # 13, 15, 14
#
# # int variable
# a = 10
# b = 11
# c = 12
#
# # abc(a, b, c) # we are calling a fun...
# # # abc(10, 11, 12)
# #
# # print(a, b, c) # 10, 11, 12
#
# # abc(b, c, a) # ...
#
# abc(c-1, b + 1, a*2) # ...


x = 10
print(x) # 1 ===> 10

def change_value(x):
    x = x + 1
    return x

# you can't use both at the same time
# def change_value_1(x): # Name 'x' is used both as a parameter and as a global
#     global x
#     x = x + 1
#     print(x)

x = change_value(x) # x = 11
# change_value_1(x)
print(x) # 2 ==> 11
