"""
Ask the user for a number and determine whether the number is prime or not.
"""

p = int(input("Enter a number "))
n = [a for a in range(2, p) if p % a == 0]


# function to find a prime number
def prime_num(x):
    if p > 1:
        if len(n) == 0:
            print(f"{x} is a prime number")
        else:
            print(f"{x} is not a prime number")
    else:
        print(f"{x} is not a prime number")


prime_num(p)
