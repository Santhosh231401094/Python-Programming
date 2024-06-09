a=int(input())
b=int(input())
c=int(input())
x=a**2
y=b**2
z=c**2
if(x==y+z or y==x+z or z==y+x):
    print("yes")
else:
    print("no")  
