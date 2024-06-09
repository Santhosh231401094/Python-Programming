s1 = input().strip()
s2 = input().strip()

balanced = True

for char in s1:
    if char not in s2:
        balanced = False
        break

print(balanced)
