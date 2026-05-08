# logical operators (return bool value): and, or, not
# and
# left  right result
# True  True   True
# True  False False
# False True  False
# False False False

name = "Karan"
age = 18

result = name == "Karan" and age >= 18
print(name, result)

# Or
result = name == "Aman" or age < 18
print(name, result)

# Not (flip tool)
result = not (name == "Karan")
print(name, result)

result = not (name == "Aman")
print(name, result)

result = (name == "Karan" or name == "Aman") and age >= 18
print(name, result)

marks = 82
cond = marks >= 75 and marks <= 85
print("Grade B:", cond)

# Circuit breaker/ short-circuit evaluation
number1 = 50
number2 = 60
number3 = 120

result = number1 >= 80 and number2 <= 100 and number3 == 120
print(number1, number2, number3, result)

result = number1 <= 80 or number2 <= 100 or number3 == 120
print(number1, number2, number3, result)
