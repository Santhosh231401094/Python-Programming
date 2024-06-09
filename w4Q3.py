n=input()
s=[0]*10
for i in n:
    s[int(i)]+=1
s0=0
for j in s:
    if j==1:
        s0+=1
print(s0)
