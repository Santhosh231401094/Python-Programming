def op(arr, k):
    i, j = 0, -1
    while i < len(arr) and j < len(arr):
        if i != j and arr[j] - arr[i] == k:
            return 1
        elif arr[j] - arr[i] < k:
            j += 1
        else:
            i += 1
    else:
        return 0
t=int(input())
for x in range(t):
    n= int(input())
    arr=list(set([int(input()) for i in range(n)]))
    k=int(input())
    print(op(arr,k))
