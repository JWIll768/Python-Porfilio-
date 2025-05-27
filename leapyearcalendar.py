#inti
#If a year is divisible by 4, it is a leap year.
#However, if that year is also divisible by 100, it is not a leap year, unless
#it is divisible by 400. In that case, it is a leap year.

#Functions
def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 > 0:
        print(True)
    elif year % 400 >0:
        print(False)

#Main
is_leap_year(1900) #print False
is_leap_year(2024) #print True
is_leap_year(2000) #print True
