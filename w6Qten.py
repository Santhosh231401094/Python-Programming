def find_pivot_index(arr):
    n = len(arr)
    total_sum = sum(arr)
    left_sum = 0
    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1  

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    pivot_index = find_pivot_index(arr)
    print(pivot_index)

if __name__ == "__main__":
    main()
