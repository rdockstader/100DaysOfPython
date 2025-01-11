# this is a game that will guess the number.
import random


print("Hello, what is your name?")
name = input()

min = 1
max = 20
num_guesses = 6

secret_number = random.randint(1, 20)

print(f"hello {name}, I am thinking of a number between {min} and {max}, you have {num_guesses} to guess the number. ")

for used_guesses in range(num_guesses):
    try:
        guess = int(input("enter your guess as a number: "))
    except ValueError:
        print("Oh No! You wasted one of your guesses by entering a value that wasn't a number, please enter a number such as 1, 19, 17, etc.")

    if guess > secret_number:
        print("Your guess was too high.")
    elif guess < secret_number:
        print("Your guess was too low")
    else:
        break

if guess == secret_number:
    print(f"you win! you guessed the number correctly in {used_guesses+1} guesses!")
else:
    print(f"You lost by using all your guesses!! the secret number was {secret_number}, better luck next time!")