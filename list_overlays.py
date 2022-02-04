"""
a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.


###### creating a new list and then appending the variables 'i' to c
prints the variables found in both 'a' and 'b'. worth remembering append


LIST OVERLAP


"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
# find the values that are in both lists
for i in a:
    if i in b:
        c.append(i)

print(c)
