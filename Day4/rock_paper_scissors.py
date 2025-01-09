import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("Welcome to rock paper scissors!")

should_continue = True 
while should_continue:

    player_selection_index = int(input("What do you choose? type 0 for rock, 1 for paper, or 2 for scissors, or 3 to quit. "))

    if player_selection_index == 3:
        should_continue = False 
        continue


    player_selection = options[player_selection_index]

    print("you choose:")
    print(player_selection)

    computer_selection = random.choice(options)
    print("computer choose:")
    print(computer_selection)

    # paper beats rock, rock beats scissors, scissor beats paper
    if player_selection == computer_selection:
        print("it's a draw")
    elif player_selection == paper:
        if computer_selection == rock:
            print("player wins!")
        else:
            print("computer wins!")
    elif player_selection == rock:
        if computer_selection == scissors:
            print("player wins!")
        else:
            print("computer wins!")
    elif player_selection == scissors:
        if computer_selection == paper:
            print("player wins!")
        else:
            print("computer wins!")