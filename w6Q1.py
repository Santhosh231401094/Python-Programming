def is_strictly_increasing(nums):
    return all(nums[i] < nums[i+1] for i in range(len(nums) - 1))

def is_strictly_decreasing(nums):
    return all(nums[i] > nums[i+1] for i in range(len(nums) - 1))

def can_be_made_strictly_ascending_or_descending(nums):
    n = len(nums)
    if is_strictly_increasing(nums) or is_strictly_decreasing(nums):
        return True
    for i in range(n):
        new_nums = nums[:i] + nums[i+1:]
        if is_strictly_increasing(new_nums) or is_strictly_decreasing(new_nums):
            return True
    
    return False

def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    result = can_be_made_strictly_ascending_or_descending(nums)
    print(result)

if __name__ == "__main__":
    main()
