print("Welcome to Python Pizza Deliveries!")
size = input("what size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on yoru pizza? Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    bill += 2

if pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 1

if(extra_cheese == "Y"):
    bill += 1


print(f"Your bill for the pizza is ${bill}.")