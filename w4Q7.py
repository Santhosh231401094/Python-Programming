a=int(input())
b=0
c=1
if a>2:
    for i in range(0,a-2):
        d=b+c
        b=c
        c=d
    print(d)
elif a==1:
    print(b)
elif a==2:
    print(c) 
