a=int(input())
b=a
i=0
c=0
while a!=0:
    a=a//10
    i=i+1
a=b
while a!=0:
    c=c+(a%10)**i
    a=a//10
    i=i-1
if(b!=c):
    print("No")
else:
    print("Yes")
