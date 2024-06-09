def compare_strings(str1, str2):
    str1 = str1.lower()  # Convert str1 to lowercase
    str2 = str2.lower()  # Convert str2 to lowercase
    if str1 < str2:
        return "-1"
    elif str1 > str2:
        return "1"
    else:
        return "0"

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the two strings
    str1 = input()
    str2 = input()
    
    # Compare the strings and print the result
    print(compare_strings(str1, str2))
