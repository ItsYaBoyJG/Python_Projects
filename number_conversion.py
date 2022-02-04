"""
Program that converts a binary/decimal number to a binary or decimal number

"""

user_number = int(input("Enter a number: "))


def Binary_to_Decimal():
    decimal_number = user_number
    i, j = 0, 0
    while decimal_number != 0:
        k = decimal_number % 10
        i = i + k * pow(2, i)
        decimal_number = decimal_number // 10
        j += 1
    print(f'The Binary value converted to Decimal is: {i}')


''''''


def Decimal_to_Binary():
    binary_number = bin(int(user_number)).replace("0b", "")
    print(f'The Decimal number in Binary is: {binary_number}')


if __name__ == '__main__':
    Binary_to_Decimal()
    Decimal_to_Binary()
