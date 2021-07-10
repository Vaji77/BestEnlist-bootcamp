# Convert a string to datetime
import datetime
def convert(date_time):
    format = '%b %d %Y %I:%M%p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str
date_time = 'OCT 12 2000 09:30AM'
print("String:",date_time)
print("Date Time:",convert(date_time))



# Subtract five days (last working day) from current date
from datetime import date, timedelta
delta = date.today() - timedelta(5)
print('Current Date:',date.today())
print('5 days before Current Date(last working day):',delta)



# Convert the date to datetime using a function
from datetime import datetime
dt = date.today()
print("Date:",dt)
print("DateTime:",datetime.combine(dt, datetime.min.time()))



# Print next 7 days (week) starting from today
import datetime
base = datetime.datetime.today()
print("NEXT 7 DAYS-:")
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))