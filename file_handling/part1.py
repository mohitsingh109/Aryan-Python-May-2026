# Read, Write (edit/ new)

# All the variable store and keep it memory (in RAM).
# Until the program is live it keep the data when it's end
# we'll lose all the data

# Why File Handling?
# File allow to store data permanently.

# Operation
# 1. open a file
# 2. Read data from a file
# 3. write data to a file
# 4. Append data to a file
# 5. close the file

# Open a file
# open(<file path>, mode)
file = open("student.txt", "r") # r = read mode
# read() => read the full content at once
# content = file.read()
# print(content)

# read one line at a time
# print(file.readline())
# print(file.readline())

# read all line into a list
lines = file.readlines()
print(lines)

file.close()