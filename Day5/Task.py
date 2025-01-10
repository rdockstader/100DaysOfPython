# make a function to replicate the max function

numbers = [123, 432, 12, 98, 123, 43, 98, 689, 98, 1, 2, 3, 4, 8, 9, 7, 9, 123, 543, 678, 98, 879, 98, 67, 987, 78]

print(max(numbers))

max_num = 0
for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)
