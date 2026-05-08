# Arithmetic operator
# +, -, /, *, %, (//, **)

a = 35
b = 20
c = a + b
print("a + b =", c)
c = a - b
print("a - b =", c)
c = a * b
print("a * b =", c)
c = a / b
print("a / b =", c) # it gives float value as well
c = a // b
print("a // b =", c) # it won't give float value
c = a ** 4 # a ^ 4
print("a ** b =", c)
c = a % b
print("a % b =", c)

# BODMAS
# * / both are at same level ( L to R )
# +, - both are at same level ( L to R )
result = 10 - 5 * 3 / 2 + 15/7/2 + 1
#        10 - 7.5 + 1.0714.... + 1
print("result =", result) # 10.3??