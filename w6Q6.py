def find_element_locations(arr, target):
    locations = []
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            locations.append(i + 1)  # Store 1-based index
            count += 1
    
    if count > 0:
        for loc in locations:
            print(f"{target} is present at location {loc}.")
        print(f"{target} is present {count} times in the array.")
    else:
        print(f"{target} is not present in the array.")

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    target = int(input())
    find_element_locations(arr, target)

if __name__ == "__main__":
    main()
