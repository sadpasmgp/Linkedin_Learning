# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library

from datetime import datetime
import time
import pendulum

# TODO: create a new datetime using pendulum
dt1 = pendulum.datetime(2020, 7, 29, tz="America/New_York")
print(dt1)

print(isinstance(dt1, datetime))

print(dt1.timezone.name)

# TODO: convert the time to another time zone
dt2 = dt1.in_timezone("Europe/Paris")
print(dt2)

# TODO: create a new datetime using the now() function
dt3 = pendulum.now("Europe/London")
print(dt3)
print(dt3.timezone.name)

# TODO: Use the local function function
here = pendulum.local(2020,11,25)
print(here)
print(here.timezone.name)

# TODO: Use today, tomorrow, yesterday
today = pendulum.today("Europe/London")
tomorrow = pendulum.tomorrow("Europe/Paris")
yesterday = pendulum.yesterday("Europe/London")
print(today, tomorrow, yesterday, sep='\n')

# TODO: create a datetime from a system timestamp
systime = time.time()
pend_systime = pendulum.from_timestamp(systime)
print(pend_systime)