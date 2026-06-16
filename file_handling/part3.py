# a => it keep the existing content from the file and add a new record at the end
file = open("student.txt", "a") # a = append mode

# \n ==> used for next line
file.write("Arjun\n")

file.close()