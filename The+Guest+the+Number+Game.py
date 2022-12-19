from random import *

random_number = randint(1, 100)
name = input("Hello, let's play the game!\nWhat is your name? ")

print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")

for n in range(1, 9):
    type_number = int(input())
    if type_number < 1 or type_number > 100:
        print(f"The number that you chose is out of play. {8-+n} attempts left")
    elif type_number > random_number:
        print(f"The number you chose is greater than the secret number. {8-+n} attempts left")
    elif type_number < random_number:
        print(f"The number you chose is lower than the secret number. {8-+n} attempts left")
    else:
        print(f"The number you chose is correct! It took {n} times to guessed it. Yay!")
        break

print(f"\nThe game has ended. The secret number was {random_number}")