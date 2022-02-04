"""
Write a function that takes an ordered list of numbers (a list where the elements
are in order from smallest to largest) and another number. The function decides
whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

uses binary search
"""

_list = list(input("Enter your list of numbers:  "))
_list.sort()
print('\n')


print(f'Here is your sorted list. [{_list}] \n')

add_list = (input("Is there another number you wish to add to the list? "))
print('\n')

if add_list in _list:
    print("The number/s are already in the list. ")
else:
    _list.append(add_list)
    print(f'The new list is: {_list}')

