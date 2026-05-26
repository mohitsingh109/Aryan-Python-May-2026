# 2. Tuple
# - Order (it maintain the insertion order)
# - Im-Mutable (no edit/delete/add)
# - Allow duplicate
# - We can access element via a Index (start = 0, end < len(list) )
# - Negative index (Python only)

weeks_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# for day in weeks_days:
#     print(day)

# As tuple is immutable we cannot edit/delete/add element in it
#weeks_days.append("Friday")
#weeks_days.remove("Saturday")

for index in range(len(weeks_days)):
    print(weeks_days[index])
