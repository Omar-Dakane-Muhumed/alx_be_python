# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through the rows
while row < size:
    # For each row, use a for loop to print asterisks side by side
    for col in range(size):
        print("*", end="")  # Stay on the same line
    print()  # Move to the next line after printing a row
    row += 1  # Move to the next row

