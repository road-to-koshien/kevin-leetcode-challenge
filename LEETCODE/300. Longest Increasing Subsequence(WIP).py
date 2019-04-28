# https://leetcode.com/problems/longest-increasing-subsequence/

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

max_current = 0
max_global = 0
nums = [10,9,2,5,7,101,18]

for i in range(0, len(nums)-1):
    if i == len(nums)-1:
        if nums[i] > nums[i-1]:
            max_current += 1
    else:
        if nums[i+1] > nums[i]:
            max_current += 1
        if max_global < max_current:
                max_global = max_current
        else:
            max_current = 0
print(max(max_global, max_current))

