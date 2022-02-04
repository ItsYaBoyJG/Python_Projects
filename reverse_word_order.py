"""
Write a program (using functions!) that asks the user for a long
string containing multiple words.
Print back to the user the same string, except with the words in backwards order

"""

str1 = input("Enter your string to have it reversed ")


def reverse_string(x):
    # splits the words of the string
    y = x.split(' ')
    # joins the split words of the string and reverses the order of them
    a = ' '.join(reversed(y))
    # prints reversed string
    print(a)
    # returns the string as a whole but in reverse order
    return x[::-1]


print(reverse_string(str1))

