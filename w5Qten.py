words_list = []

# Read words from the user until a blank line is entered
while True:
    word = input().strip()  # Read input and remove leading/trailing spaces
    
    
    if not word:
        break
    
  
    if word not in words_list:
        words_list.append(word)


for word in words_list:
    print(word)
