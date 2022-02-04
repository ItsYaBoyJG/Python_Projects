"""
You are given an integer, . Your task is to print an alphabet rangoli of size .
(Rangoli is a form of Indian folk art based on creation of patterns.)

"""

import string

n = int(input())


def print_rangoli(size):
    a = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        s = a[size - 1:i:-1] + a[i:size]
        print('-'.join(s).center(4 * size - 3, '-'))


print_rangoli(n)
'''

alphabet = 'zyxwvutsrqponmlkjihgfedcba'
alphabet = alphabet[-n::]
for i in range(2 * n - 1):
    if i >= n :
        i = n - i - 2
    s = alphabet[:i] + alphabet[i::-1]
    print('-'.join(s).center((4 * n - 3), '-'))

def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

'''

'''  a = string.ascii_lowercase[:size]
   for i in range(2 * size - 1):
       if i >= size:
           i = size - i - 2
       s = a[i::-1] + a[1:]
       print('-'.join(s).center((4 * size - 3), '-'))'''
