# Function to calculate the sum of integers in a list
def sum_of_integers(lst):
    return sum(int(x) for x in lst)

# Main function to process input and generate output
def process_input():
    n = int(input())  # Number of lines to read
    results = []  # Store the results before printing
    for _ in range(n):
        # Reading each line and splitting it into words
        line = input().split()
        # First word is the name, rest are integers
        name = line[0]
        integers = line[1:]
        # Calculate the sum of integers
        total = sum_of_integers(integers)
        # Store the result
        results.append((name, total))
    
    # Sort the results by total sum
    results.sort(key=lambda x: x[1])

    # Print the sorted results
    for name, total in results:
        print(name, total)

# Calling the main function
if __name__ == "__main__":
    process_input()
