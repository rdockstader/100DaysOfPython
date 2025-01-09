import sys

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer = input("Would you like to go left or right? ")

if answer.lower() == "right":
    print("You feel of a cliff, you silly goose! GAME OVER")
    sys.exit()

answer = input("You have come to a Lake. Would you like to swim across, or wait for a boat? ")

if answer.lower() == "swim":
    print("You make it halfway across the lake when you muscle begins to cramp and you drown. GAME OVER")
    sys.exit()

print("You have made it to an island. On the island there are three huts with different colored doors on them.")
answer = input("Do you want to go through the (R)ed, (B)lue, or (Y)ellow door? ")

if answer.lower() == "y":
    print("You've entered the yellow door. You've won, enjoy your imginary treasure!")
elif answer.lower() == "r":
    print("you've entered the blue door. you fall through a magic portal and are never seen again.")
else:
    print("You've entered the red door. Inside there is a three headed dog, that makes you his lunch.")