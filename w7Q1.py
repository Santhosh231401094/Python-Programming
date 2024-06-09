nums = list(map(int, input().split()))
repeated_num = None
for num in nums:
    if num in set(nums) and nums.count(num) > 1:
        repeated_num = num
        break
print( repeated_num)
