import math

def s(d,t):
    ra=d/2
    r=ra*100
   
    pa = math.pi * (r ** 2)
    ta = t ** 2
   
    tr = math.ceil(pa / ta)
    if d%2==0:
        return (tr)
    else:
        return(tr+100)
       

d, t = map(int, input().split())
print(s(d, t),"tiles")
