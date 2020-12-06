#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))


# print today's date
now = datetime.now()
print('todays date is', str(now))


# print today's date one year from now
print('one year from now', str(now+timedelta(days=365)))

# create a timedelta that uses more than one argument
print("Ïn 2 days and 3 weeks it will be " + 
str(now+timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
print("5 days 3 weeks back time was " +
str(now-timedelta(days=5, weeks=5)))

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year

if afd < today:
    print("Äpril Fool's day went by %d days ago"%((today-afd).days))

# Now calculate the amount of time until April Fool's Day  

today = date.today()
aprilfoolday = date(2021, 4, 1)
print("April fool day will occur in: %d days" % ((aprilfoolday-today).days))
