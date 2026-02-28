# arrays/arrays_basics.py

# ── Create ──────────────────────────────────────
my_array = [7, 12, 9, 4, 11]
print("Array:", my_array)

# ── Access by index (O(1)) ──────────────────────
print("Element at index 0:", my_array[0])   # 7
print("Element at index 3:", my_array[3])   # 4

# ── Update ──────────────────────────────────────
my_array[2] = 99
print("After update index 2:", my_array)    # [7, 12, 99, 4, 11]

# ── Insert at end (O(1)) ────────────────────────
my_array.append(50)
print("After append:", my_array)

# ── Insert at position (O(n) - shifts elements) ─
my_array.insert(2, 100)
print("After insert at index 2:", my_array)

# ── Delete by index (O(n) - shifts elements) ────
my_array.pop(2)
print("After pop index 2:", my_array)

# ── Loop through array ──────────────────────────
print("\nAll elements:")
for i in range(len(my_array)):
    print(f"  Index {i}: {my_array[i]}")

# ── Find lowest value (algorithm) ───────────────
min_val = my_array[0]
for val in my_array:
    if val < min_val:
        min_val = val
print("\nLowest value:", min_val)