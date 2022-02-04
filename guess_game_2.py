"""

the PC will guess the user's number.

# user's number is half the two numbers entered.
# don't really know how to make it simpler for the pc/program guess the number

"""


smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

count = 0

print()
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print('%d %d' % (smaller, larger))
    print('Your number is %d' % myNumber)
    choice = input('Enter =, <, or >: ')
    if choice == '=':
        print("Hooray, I've got it in %d tries" % count)
        break
    elif smaller == larger:
        print("I'm out of guesses, and you cheated")
        break
    elif choice == '<':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1

#num = int(input("Enter the number you wish for the "))