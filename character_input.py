"""
Asks for user input for name and age. then outputs user name as the year they will turn 100

CHARACTER INPUT
"""

# ask for name
name = input("Please enter your name ")
# ask for age
age = int(input("Enter your age "))
# figures out year age = 100
num = str((2019 - age) + 100)
# prints answer
print("Your name is " + name + " ,you will be 100 in " + num)

