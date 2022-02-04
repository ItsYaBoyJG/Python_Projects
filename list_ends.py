"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.
"""

a = input("Enter your list of numbers ( with commas) ")

l_ist = list(map(int, a.split(',')))


# l = [1, 2, 3, 4, 5, 6]


# print(l[0], l[-1])

def list_ends(x):
    return [x[0], x[len(x) - 1]]


print(list_ends(l_ist))
