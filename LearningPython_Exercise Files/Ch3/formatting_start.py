#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  print(now)
  print(now.strftime('%Y'))
  print(now.strftime('%y'))
  print(now.strftime('%M'))
  print(now.strftime('%m'))
  print(now.strftime('%D'))
  print()

  print(now.strftime('%Y'))
  print(now.strftime('%y%y'))
  print(now.strftime('%MM'))
  print(now.strftime('%mm'))
  print(now.strftime('%d'))
  print()

  print(now.strftime('%a'))
  print(now.strftime('%A'))
  print(now.strftime('%b'))
  print(now.strftime('%B'))
  print(now.strftime('%c'))
  print()

  print(now.strftime('%I'))
  print(now.strftime('%H'))
  print(now.strftime('%p'))
  print(now.strftime('%X'))

  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month


  # %c - locale's date and time, %x - locale's date, %X - locale's time


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  

if __name__ == "__main__":
  main()
