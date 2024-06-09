from collections import defaultdict

def count_pairs(t, k):
    # Step 1 and 2
    count_dict = defaultdict(int)
    for num in t:
        count_dict[num] += 1

    # Step 3
    pair_set = set()

    # Step 4
    for num in t:
        if k - num in count_dict and count_dict[k - num] > 0:
            pair = tuple(sorted((num, k - num)))
            if pair not in pair_set:
                pair_set.add(pair)
                count_dict[num] -= 1

    # Step 5
    return len(pair_set)

# Get t and k as input
t_str = input()
k = int(input())
t = tuple(map(int, t_str.split(',')))

# Call the function with t and k as input
print(count_pairs(t, k))
