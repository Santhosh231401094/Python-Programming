def uncommon_words(s1, s2):
    # Function to parse a sentence and return a dictionary of word counts
    def parse_sentence(sentence):
        word_count = {}
        words = sentence.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count
    
    # Parse both sentences
    s1_word_count = parse_sentence(s1)
    s2_word_count = parse_sentence(s2)
    
    # Initialize list to store uncommon words
    uncommon_words = []
    
    # Check for uncommon words in s1
    for word, count in s1_word_count.items():
        if count == 1 and word not in s2_word_count:
            uncommon_words.append(word)
    
    # Check for uncommon words in s2
    for word, count in s2_word_count.items():
        if count == 1 and word not in s1_word_count:
            uncommon_words.append(word)
    
    return ' '.join(uncommon_words)

# Example usage
s1 = input("")
s2= input ("")

print(uncommon_words(s1, s2))
