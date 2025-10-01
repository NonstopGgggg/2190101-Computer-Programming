# We are to make 5 functions as instructed.
mname = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: 
      return True
    return False

def read_date():
    # Read the day, month, and year separated by space.
    # Return a list containing the day, month, and year.
    date = input().split()
    
    for i in range(12):
      if date[1] == mname[i]:
        date[1] = i+1
        
    return [int(i) for i in date]

def zodiac(day,month):
    # Return the zodiac sign given the day (d) and month (m).
    zodiac = ""
    
    if (day >= 22 and month == 3) or (day <= 21 and month == 4):
        zodiac = "Aries"
    elif (day >= 22 and month == 4) or (day <= 21 and month == 5):
        zodiac = "Taurus"
    elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
        zodiac = "Gemini"
    elif (day >= 22 and month == 6) or (day <= 21 and month == 7):
        zodiac = "Cancer"
    elif (day >= 22 and month == 7) or (day <= 21 and month == 8):
        zodiac = "Leo"
    elif (day >= 22 and month == 8) or (day <= 21 and month == 9):
        zodiac = "Virgo"
    elif (day >= 22 and month == 9) or (day <= 21 and month == 10):
        zodiac = "Libra"
    elif (day >= 22 and month == 10) or (day <= 21 and month == 11):
        zodiac = "Scorpio"
    elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
        zodiac = "Sagittarius"
    elif (day >= 22 and month == 12) or (day <= 20 and month == 1):
        zodiac = "Capricorn"
    elif (day >= 21 and month == 1) or (day <= 20 and month == 2):
        zodiac = "Aquarius"
    elif (day >= 21 and month == 2) or (day <= 21 and month == 3):
        zodiac = "Pisces"

    return zodiac

def days_in_feb(y):
    # Return the number of days in February of the given year (y).
    if leap_year(y):
      return 29
    return 28

def days_in_month(m,y):
    # Return the number of month given the month (m) and year (y).
    if m != 2:
      return days_month[m-1]
      
    else:
      return days_in_feb(y)

def days_in_between(d1,m1,y1,d2,m2,y2):
    # Return the number of days from d1, m1, and y1 to d2, m2, and y2.
    day_between = 0
    
    # We are going to calculate days in between by separating this calculation into three parts
    # the start date to the end of y1
    day_between += days_month[m1-1] - d1 + 1 # the birth month where the first date is included.
    day_between += sum(days_month[m1:]) # the month after birth
    
    if m1 <= 2 and leap_year(y1): # account for leap year
        day_between += 1
    
    # the start of y1 + 1 to the before the start of y2
    year = y2-y1-1
    day_between += int(year * 365.25)
        
    # the start of y2 to the end date
    day_between += sum(days_month[:m2-1]) # days until the last month
    day_between += d2 - 1 # days in last month
    
    if m2 > 2 and leap_year(y2): # account for leap year
        day_between += 1

    return day_between

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    # Display the zodiac sign of d1, m1, y1, and d2, m2, y2
    # on the same line, separated by space.
    print(zodiac(d1,m1),zodiac(d2,m2))
        
    # Display the number of days from d1, m1, and y1 to d2, m2, and y2.
    print(days_in_between(d1,m1,y1,d2,m2,y2))
    
    return

exec(input().strip()) # This line is required for grader to work.
