# views = [100, 200, 20, 40, 400, 560]
# sorted_views = sorted(views)
# print(sorted_views[-3:])

student_marks = {
    "Mohit": 70,
    "Karan": 55,
    "Aman": 99,
    "Aryan": 97
}

#print(student_marks.items()) # [ ("Mohit", 70), ("Karan", 55) ]

# lambda
                                    # ("Mohit", 70)
values = sorted(student_marks.items(), key=lambda item: item[1], reverse=True)
print(values)
top2_student = values[0:2]
for item in top2_student:
    print(item[0])

# print(top2_student)
# # [("1234", {"likes": 40, "views": 70, ...}), ...]
# #sorted(video_info.items(), key=lambda item: item[1]["views"] + item[1]["likes"])
# values_dict = dict(sorted(student_marks.items(), key=lambda item: item[1]))
# print(values_dict)

views = [100, 200, 20, 40, 400, 560]
sorted_views = sorted(views, reverse=True) # Deceasing order
print(sorted_views)
print(sorted_views[:3])