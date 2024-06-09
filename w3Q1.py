a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print("That's a equilateral triangle")
elif a==b!=c or a==c!=b or b==c!=a:
    print("That's a isosceles triangle")
else:
    print("That's a scalene triangle")
