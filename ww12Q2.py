def count_pairs_with_difference(n, nums, k):
    # Dictionary to count the occurrences of each activity number
    activity_count = {}
    
    # Populate the dictionary with counts
    for num in nums:
        if num in activity_count:
            activity_count[num] += 1
        else:
            activity_count[num] = 1
    
    # Variable to count the number of valid pairs
    pair_count = 0
    
    # Iterate through the unique activity counts
    for num in activity_count:
        if k == 0:
            # Special case when k is 0, we look for pairs of the same number
            if activity_count[num] > 1:
                pair_count += (activity_count[num] * (activity_count[num] - 1)) // 2
        else:
            # General case: look for pairs with difference k
            if num + k in activity_count:
                pair_count += activity_count[num] * activity_count[num + k]
            if num - k in activity_count:
                pair_count += activity_count[num] * activity_count[num - k]
    
    # Since each pair (i, j) is counted twice in the general case, we need to halve the result
    if k != 0:
        pair_count //= 2
    
    return pair_count

# Example input
n = int(input().strip())
nums = list(map(int, input().strip().split()))
k = int(input().strip())

# Calculate and print the result
print(count_pairs_with_difference(n, nums, k))
