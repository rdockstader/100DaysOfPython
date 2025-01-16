import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
num_chances = 6
correct_guesses = []
wrong_guesses = []
while len(wrong_guesses) < num_chances and len(correct_guesses) < len(chosen_word):

    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    if guess in chosen_word:
        correct_guesses.append(guess)
        print("you guessed right!")
    else:
        wrong_guesses.append(guess)
        print("You guessed Wrong :(")

    for letter in chosen_word:
        if letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)
    print(f"You've used {len(wrong_guesses)}/{num_chances} guesses")

if len(correct_guesses) == len(chosen_word):
    print("You got the word, congrats!!")
else:
    print(f"Sorry, you failed to guess the word! it was {chosen_word}")