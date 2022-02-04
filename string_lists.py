"""
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)

STRING LISTS
"""

word = input("Enter a string: ")

# reverse's string
str1 = word[::-1]

if word == str1:
    print(str1)
    print(f"Your string, {word}, is a palindrome!! ")

# string formatting
# returns decimal, octal, hex(capitalized) and binary
# forms of numbers between i and inputted number


num = input("Enter a number: ")
n = int(num)


def form_string(x):
    w = len(f'{x:b}')
    for i in range(x):
        print(f'{i:>{w}} {i:>{w}o} {i:>{w}X} {i:>{w}b}')


form_string(n)
