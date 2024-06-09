def find_intersection(array1, array2):
    i, j = 0, 0
    intersection = []
    
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            intersection.append(array1[i])
            i += 1
            j += 1
        elif array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    
    return intersection
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N1 = int(data[index])
        index += 1
        array1 = list(map(int, data[index:index+N1]))
        index += N1
        
        N2 = int(data[index])
        index += 1
        array2 = list(map(int, data[index:index+N2]))
        index += N2
        
        # Find intersection of the two arrays
        intersection = find_intersection(array1, array2)
        
        # Append the intersection result to the results list
        results.append(" ".join(map(str, intersection)))
    
    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
