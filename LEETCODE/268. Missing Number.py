# https://leetcode.com/problems/missing-number/

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution(object):
    def missingNumber(self, nums):
        if 0 not in nums:
            return 0
        nums.sort()
        for i,each in enumerate(nums):
            if i == len(nums)-1:
                return nums[-1] + 1
            if nums[i+1] - nums[i] != 1:
                return nums[i]+1