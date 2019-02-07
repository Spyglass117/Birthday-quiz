"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name

#Gets variables from user
name = input("Hello, what is your name?")
birthmonth = str.lower(input("Hi {0}, what was the name of the month you were born in?".format(name)))
birthyear = int(input("And what year were you born in, {0}?".format(name)))
birthday = int(input("And the day?"))

#Translates user inputs into month numbers
monthnames = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
monthabr = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
if birthmonth in monthnames:
    monthindex = monthnames.index(birthmonth)
    monthlocation = monthindex + 1
elif birthmonth in monthabr:
    monthindex = monthabr.index(birthmonth)
    monthlocation = monthindex + 1
else:
    print ("Invalid Month Input")

#Gets current time data
todaymonth = datetime.today().month
todayyear = datetime.today().year
todayday = datetime.today().day

#Checks to see if entered birthdate is in the future
if birthyear > todayyear:
    print("You have not been born yet!")

#Checks user birth date against holidays
elif monthlocation == 10 and birthday == 31:
    print("You were born on Halloween!")
elif monthlocation == 12 and birthday == 25:
    print("You were born on Christmas!")

#Checks user birth date against year and month to find "birth block"