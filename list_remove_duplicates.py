"""
Write a program that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

"""

a = [1, 1, 2, 3, 5, 5, 11, 13, 13, 15, 16, 16, 18,18]
b = [1, 2, 3, 5, 6, 7, 8, 9, 10]
c = []

# find the values that are in both lists
for i in a:
    if i not in b:
        c.append(i)

print(c)
