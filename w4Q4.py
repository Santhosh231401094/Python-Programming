n=int(input())
m=[]
o=0
while n!=0:
    d=n%10
    n=n//10
    if(d not in m):
        m.append(d)
        o+=1
print(o)
