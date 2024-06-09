def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap is made
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr

# Reading input
num_elements = int(input())
arr = list(map(int, input().split()))

# Sorting the array using bubble sort
sorted_arr = bubble_sort(arr)

# Printing the sorted array
print(" ".join(map(str, sorted_arr)))
