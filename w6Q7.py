def merge_arrays(array1, array2):
    # Convert arrays to sets to remove duplicates
    set1 = set(array1)
    set2 = set(array2)
    
    # Merge the sets to get unique elements from both arrays
    merged_set = set1.union(set2)
    
    # Convert the merged set back to a sorted list
    merged_list = sorted(merged_set)
    
    return merged_list
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    # Number of elements in array 1
    N1 = int(data[index])
    index += 1
    
    # Elements of array 1
    array1 = []
    for _ in range(N1):
        array1.append(int(data[index]))
        index += 1
    
    # Number of elements in array 2
    N2 = int(data[index])
    index += 1
    
    # Elements of array 2
    array2 = []
    for _ in range(N2):
        array2.append(int(data[index]))
        index += 1
    
    # Merge arrays and get the sorted merged array without duplicates
    merged_array = merge_arrays(array1, array2)
    
    # Print the merged array as the output
    print(" ".join(map(str, merged_array)))

if __name__ == "__main__":
    main()
