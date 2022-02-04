"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.


GUESSING GAME ONE
"""

import random

# get user input
guess = int(input("Guess a number between 1 and 9. "))
# guess = 0
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rdm = random.randint(1, 9)
print(rdm)


# to solve guess if correct
def rdm_guess(x):
    while x != rdm:
        # guess = int(input("Guess a number between 1 and 9. "))
        if x < rdm:
            return print("You guessed too low")
        elif x > rdm:
            return print("You guessed too high")
        else:
            return print("You guessed right")


# invalid input
if guess > 9 or guess < 1:
    print("Enter a guess between 1 and 9")
    print(guess)

rdm_guess(guess)

# endgame or restart
