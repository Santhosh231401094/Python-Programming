S1 = input().strip()
S2 = input().strip()
N = int(input().strip())

common_chars = ""
seen_chars = set()

for char in S1:
    if char in S2 and char not in seen_chars:
        common_chars += char
        seen_chars.add(char)
        if len(common_chars) == N:
            break

print(common_chars)

