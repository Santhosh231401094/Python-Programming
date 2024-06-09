def categorize_books():
    # Initialize an empty dictionary to store books by genre
    library = {}

    
    
    while True:
        try:
            # Read a line of input
            line = input().strip()
            
            # Check for the blank line which indicates end of input
            if not line:
                break
            
            # Split the input into book title and genre
            if ',' in line:
                title, genre = map(str.strip, line.split(',', 1))
                
                # Add the book title to the appropriate genre in the dictionary
                if genre not in library:
                    library[genre] = []
                library[genre].append(title)
            else:
                print("Invalid input format. Please enter in 'title, genre' format.")
        except EOFError:
            break

    # Print the categorized books by genre
    for genre, titles in library.items():
        print(f"{genre}: {', '.join(titles)}")

# Call the function to execute the program
categorize_books()
