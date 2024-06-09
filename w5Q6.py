a=input()
a=a.lower()
b=a.split(' ')
#print(b)

for i in range(len(b)):
 p=b[i]
 if p!=p[::-1]:
  print(b[i],end=' ')
