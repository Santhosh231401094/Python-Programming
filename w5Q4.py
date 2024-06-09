string1 = input().strip()
string2 = input().strip()

index = -1

for i in range(len(string1)):
    if string1[i:i+len(string2)] == string2:
        index = i
        break

print(index)
