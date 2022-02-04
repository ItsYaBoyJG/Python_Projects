"""

program that determines leap years
"""
import calendar

year = int(input("Enter year: "))


def is_leap(x):
    #   if x % 4 == 0:
    #     if x % 400 == 0 and x % 100 == 0:
    #         print(f'{x} is a leap year. ')
    #  else:
    # print(f'{x} is not a leap year. ')
    if calendar.isleap(x):
        print(f'{x} is a leap year. ')
    else:
        print(f'{x} is not a leap year. ')


is_leap(year)
