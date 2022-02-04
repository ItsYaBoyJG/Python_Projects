import math


def ask():
    while True:
        try:
             n = int(input("Enter an Integer"))
        except:
            print("An error occured")
            continue
        else:
            break
    print("Your number squared is ", n ** 2)

ask()





