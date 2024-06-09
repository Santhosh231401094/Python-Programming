a=int(input())
b=int(input())
c=int(input())
d=a+b+c
if(a<=65 and b>=55 and c>=50):
    print("The candidate is eligible")
elif(d>=180):
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")
