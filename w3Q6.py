def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input())


if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
