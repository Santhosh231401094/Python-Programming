x=int(input())
y=int(input())
z=int(input())
if(z>(x+y)):
    gain=z-(x+y)
    gainpercent=(gain/(x+y))*100
    print("{:.2f}".format(gainpercent),"is the gain percent.")
