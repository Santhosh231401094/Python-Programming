def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element was not present
    return -1

# Reading input
arr = list(map(int, input().split(',')))
x = int(input())

# Ensure the array is sorted
arr.sort()

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("True")
else:
    print("False")


