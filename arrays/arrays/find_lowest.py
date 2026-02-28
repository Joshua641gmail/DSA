my_array = [5, 3, 8, 1, 4]
min_val = my_array[0]

for i in my_array:
    if i < min_val:
        min_val = i

print("Lowest value:", min_val)