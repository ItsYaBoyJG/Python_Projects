"""
program that creates a matrix

"""

from numpy import identity
from numpy import eye

while True:
    try:
        a = int(input("Enter the size of the square matrix you wish to make. \n"
                      "Size: "))
    except ValueError:
        print("You did not enter an integer, please try again. ")
        continue
    else:
        print(identity(a))
        break
while True:
    try:
        x, y, z = map(int, input("Enter your 2D array, along with "
                                 "diagonal if wanted. (with spaces)\n"
                                 "Size: ").split())
    except ValueError:
        print("You did not enter an integer, please try again. ")
        continue
    else:
        print(eye(x, y, k=z))
        break
