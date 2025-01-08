print("Welcome to the tip calculator!")
bill = float(input("What was the total Bill? $"))
tip = int(input("How much would you like to tip? 10, 12, 15 "))
nunber_of_people = int(input("How many people are splitting the bill? "))

tip_percent = tip / 100
total_bill = bill * (1 + tip_percent)

cost_per_person = round(total_bill/nunber_of_people)

print(f"each person should pay ${cost_per_person}")