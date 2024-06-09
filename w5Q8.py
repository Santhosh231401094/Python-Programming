input_string = input()

# Initialize counts
letters = 0
digits = 0
specials = 0

# Count the characters
for char in input_string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        specials += 1

# Print the results
print(letters)
print(digits)
print(specials)
