# Datetime module
# used for dates and time

import datetime

now = datetime.datetime.now() # date + time
print(now)
print(now.strftime("%d/%m/%Y"))

today = datetime.date.today()
print(today)