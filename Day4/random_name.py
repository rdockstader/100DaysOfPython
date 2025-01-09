import random

friends = ["Jim", "Dwight", "Stanley", "Phillis", "Angela", "Pam", "Michael"]


# the way I did it
random_index = random.randint(0, len(friends) - 1)
print(friends[random_index])

# the python way
print(random.choice(friends))