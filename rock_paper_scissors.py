"""
 a two-player Rock-Paper-Scissors game.

ROCK PAPER SCISSORS
"""

import random

print("Let's Play Rock Paper Scissors!! \n")
play = input("Enter your choice \n")

hand = ['rock', 'paper', 'scissors']

cpu_choice = random.choice(hand)


# not equal
# if play != 'rock' or 'paper' or 'scissors':
#   print("Please enter a correct choice ", input)


# is it equal to
def rock_paper_scissors(x):
    while x == 'rock' or 'paper' or 'scissors':
        if x == 'rock' and cpu_choice == 'scissors':
            print("You win")
        if x == 'paper' and cpu_choice == 'rock':
            print("You win")
        if x == 'scissors' and cpu_choice == 'paper':
            print("You win")
        elif x == 'scissors' and cpu_choice == 'rock':
            print("You lose")
        elif x == 'rock' and cpu_choice == 'paper':
            print("You lose")
        elif x == 'paper' and cpu_choice == 'scissors':
            print("You lose")
        break


rock_paper_scissors(play)


# ask user to play again