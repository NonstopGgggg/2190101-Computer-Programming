# We are to print the calendar of a particular month of a particular year
# However, we have to take into account the starting day of the month and the number of days in the month
# Moreover, leap year has to be considered as well T-T
# Let's say 1st january 0001 is a Monday

def leap_year_count(y):
    # We minus the year by 1 to exclude the current year
    year = y-1

    # Leap year occurs every 4 years except for years that are divisible by 100 but not divisible by 400
    # In a period of hundreds of years, there will be 25 - 1 = 24 leap years.
    # In a period of 400 years, there will be (25 * 4) - 4 + 1 = 97 leap years because the year divisible by 400 is also a leap year
    return (year//4) - (year//100) + (year//400)

def start_day(m,y):
    # let 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
    # Every year move the day of the week by 1 (2 for leap year)
    # Find the first day of the week of month m of year y
    leap = leap_year_count(y)
    dayOfWeek = ((y-1) * 365 + leap) % 7
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(m-1):
        dayOfWeek = (dayOfWeek + month_days[i]) % 7

        if m == 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
            dayOfWeek = (dayOfWeek + 1) % 7

    return dayOfWeek

def print_month(m,y):
    # Find the start date of the month
    start = start_day(m,y)

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_days = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]

    # Check for leap year
    if m == 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
            month_days[1] = 29

    # Print the header of the calendar with consistent left padding (4 in this case)
    for i in range(7):
        print(" "*(2) + week_days[i],end='')

    print("")

    # Print the leading spaces for the first week
    # If the day starts on Sunday, no leading spaces are needed
    if start != 6:
        print(" " * (4 * (start+1)),end="")

    for i in range(1,month_days[m-1]+1):

        if (i + start) % 7 == 0:
            print("")
    
        print(" " * (4 - len(str(i))), end='')
        print(i,end='')

print_month(8,2019)
