def find_mapping(A, B):
    # Step 1: Create a dictionary to map elements of B to their indices
    index_map = {}
    for idx, value in enumerate(B):
        index_map[value] = idx
    
    # Step 2: Create the index mapping P based on A and index_map
    P = []
    for value in A:
        P.append(index_map[value])
    
    return P
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    # Number of elements in A and B (should be equal)
    n = int(data[index])
    index += 1
    
    # Elements of list A
    A = []
    for _ in range(n):
        A.append(int(data[index]))
        index += 1
    
    # Elements of list B
    B = []
    for _ in range(n):
        B.append(int(data[index]))
        index += 1
    
    # Find the index mapping P from A to B
    P = find_mapping(A, B)
    
    # Print the result as space-separated integers
    print(" ".join(map(str, P)))

if __name__ == "__main__":
    main()
