import random

randomNumber = random.randint(1, 9)

chances = 5

print("This is a random number guessing game, guess a number between 1-9")
while chances != 0:
    guess = input("Enter Your guess: ")

    guess = int(guess)

    if guess == randomNumber:
        print("You Got it right congrats!")
        break

    elif guess > randomNumber:
        print("To High!")

    elif guess < randomNumber:
        print("To Low!")

    chances-=1
if chances == 0:
    print("Oh well, you lost, the number was", randomNumber )
