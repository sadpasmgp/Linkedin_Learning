#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print(f"todays date is {today}")
  
  # print out the date's individual components
  print("Date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("todays week day is: ", today.weekday())
  days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
  print("Today is : ", days[today.weekday()])

  print(datetime.now())
  t = datetime.time(datetime.now())

  print(t)

if __name__ == "__main__":
  main()
  