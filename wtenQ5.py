from collections import Counter

# Reading input
arr = list(map(int, input().split()))

# Counting the frequency of each number
frequency = Counter(arr)

# Sorting the numbers
sorted_numbers = sorted(frequency.keys())

# Printing the numbers with their frequencies
for number in sorted_numbers:
    print(number, frequency[number])
