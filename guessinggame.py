from calendar import c
import random
number=random.randint(1,9)
chance=0
print("Guess a number between 1 and 9")
while chance <5:
    guess=int(input("Enter your guess="))
    if guess==number:
        print("You have guessed correct! Woohooo")
        break
    elif guess <number:
        print("Your guess was too low!:(")
    else:
        print("Your guess was too high!:(") 
    chance=chance+1
if not chance <5:
    print("YOU LOSE!!! the number is",number)

