n=int(input())
for i in range(2,n):
    if(n%i==0):
        b=1
        break
    else:
        b=2
print(b)
