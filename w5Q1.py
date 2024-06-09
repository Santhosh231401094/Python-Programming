sentence = input()
words = sentence.split()

longest_word = ""
longest_length = 0

for word in words:
    if len(word) > longest_length:
        longest_word = word
        longest_length = len(word)

print(longest_word)
print(longest_length)
