s = input().strip()
output = []

i = 0
while i < len(s):
    char = s[i]
    count = ""
    i += 1
    while i < len(s) and s[i].isdigit():
        count += s[i]
        i += 1
    output.append(char * int(count))

print(''.join(output))

