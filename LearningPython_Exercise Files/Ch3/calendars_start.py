#
# Example file for working with Calendars
#

# import the calendar module
import calendar


# create a plain text calendar
c = calendar.TextCalendar()
st = c.formatmonth(2020, 1, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar()
st = hc.formatmonth(2020, 1)
print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2020, 1):
    print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)
# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

