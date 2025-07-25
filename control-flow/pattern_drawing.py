# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Outer loop (while) - controls the number of rows
while row < size:
    # Inner loop (for) - prints asterisks in one row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
