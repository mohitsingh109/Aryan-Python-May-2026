integers = [40,30,42,90,45,62]

def find_max_value():
    result = -1
    for value in integers:
        if value > result:
            result = value
    return result

print( find_max_value() )

def find_max_value_index():
    max_value = 0
    max_index = -1
    for i in range(len(integers)):
        if integers[i] > max_value:
            max_value = integers[i]
            max_index = i

    return max_value, max_index

print(find_max_value_index())


