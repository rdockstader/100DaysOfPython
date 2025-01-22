def calculate_love_score(name1, name2):
    love = "love"
    true = "true"
    true_count = 0
    love_count = 0
    name1 = name1.lower()
    name2 = name2.lower()
    for char in name1: 
        if char in love:
            love_count += 1
        if char in true:
            true_count += 1 
    for char in name2: 
        if char in love:
            love_count += 1
        if char in true:
            true_count += 1 
    print(f"{true_count}{love_count}")
    
    
calculate_love_score("Kanye West", "Kim Kardashian")