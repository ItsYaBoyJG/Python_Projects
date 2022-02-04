"""
asks for user input then prints out if the number is even or odd


"""

# function to find if even or odd
def result(num1):
    if num1 % 2 == 0:
        print("even")
    else:
        print("odd")

num = int(input("Enter a number "))

result(num)