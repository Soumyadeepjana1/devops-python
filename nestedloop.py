# Nested Loops Example
# A nested loop is a loop inside another loop

print("Multiplication Table (1 to 5):")
print("=" * 30)

# Outer loop for rows
for i in range(1, 6):
    # Inner loop for columns
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product:2d}", end="  ")
    print()  # New line after each row
    print()  # Empty line for spacing

print("=" * 30)
print("Pattern using nested loops:")
print()

# Another example: Print a right-angle triangle pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
