"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number

DIVISORS

"""

# find the divisors of a number
x = int(input("Enter a number"))
a = list(range(1, x + 1))
divisor = []
for number in a:
    if x % number == 0:
        divisor.append(number)


print(divisor)

# def divisors()
