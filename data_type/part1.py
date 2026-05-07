# Data type

# string "Mohit Singh"
# char 'M'
# float/double: 34.6
# int: 45
# boolean: True/False

# Dynamic Type language
# variable = value
name = "Aryan" # str
rating = 4.9 # float/double
is_playing = True # boolean
age = 24 # int

# CMD + / for comment or uncomment a line
# print(name, type(name))
# # name = 12345 # Dynamic Type language it changes itself to int type
# # print(name, type(name))
# print(rating, type(rating))
# print(is_playing, type(is_playing))
# print(age, type(age))

# Str ==> Float
amount = "2345.87"
print(amount, type(amount)) #2345.87, str
amount_f = float(amount)
print(amount_f, type(amount_f)) #2345.87, float

# Str ===> int
amount = "3344"
print(amount, type(amount))
amount_i = int(amount)
print(amount_i, type(amount_i))

# Float ==> int
weight = 44.67
print(weight, type(weight))
weight_i = int(weight)
print(weight_i, type(weight_i))

# Float ==> str
ratings = 5.9
print(ratings, type(ratings))
ratings_s = str(ratings)
print(ratings_s, type(ratings_s))

# Str ==> Float
# product_name = "IPhone"
# # Run time error
# product_name_f = float(product_name) # Value error
# print(product_name_f, type(product_name_f))
