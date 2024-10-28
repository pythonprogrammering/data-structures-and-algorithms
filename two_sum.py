# 1. Brute Force Approach
# This approach checks each possible pair of numbers to see if they add up to the target.
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  # Return None if no solution found


# 2. Dictionary approach
# This approach uses a hash map (dictionary) to store each number and its index for faster lookups.
# We only really need to know if the complement exists.
def two_sum_hash_map(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None  # Return None if no solution found


# Example usage
nums = [2, 7, 11, 15]
target = 9

print("Brute Force Result:", two_sum_brute_force(nums, target))  # Output: [0, 1]
print("Hash Map Result:", two_sum_hash_map(nums, target))  # Output: [0, 1]
