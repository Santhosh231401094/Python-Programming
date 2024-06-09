letter_points = {
    'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

# Function to calculate Scrabble score for a word
def calculate_scrabble_score(word):
    score = sum(letter_points.get(letter.upper(), 0) for letter in word)
    return score

# Input word
word = input("")

# Calculate Scrabble score
score = calculate_scrabble_score(word)

# Output the result
print(f"{word} is worth {score} points.")
