def find_peaks(arr):
    n = len(arr)
    peaks = []

    for i in range(n):
        # Check if the element is a peak
        if (i == 0 and arr[i] >= arr[i + 1]) or \
           (i == n - 1 and arr[i] >= arr[i - 1]) or \
           (0 < i < n - 1 and arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
            peaks.append(arr[i])
    
    return peaks

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Finding peak elements
peaks = find_peaks(arr)

# Printing peak elements
print(" ".join(map(str, peaks)))
