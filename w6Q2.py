a=list(set([int(input()) for x in range(10)]))
I=int(input())
print("ITEM to be inserted:{}".format(I))
a.append(I)
a.sort()
print("After insertion array is:")
for z in a:
    print(z)
