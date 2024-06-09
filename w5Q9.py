keywords = {'break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var'}

# Read the input string
input_string = input().strip()

# Check if the input string is a keyword
if input_string in keywords:
    print(input_string, "is a keyword")
else:
    print(input_string, "is not a keyword")
