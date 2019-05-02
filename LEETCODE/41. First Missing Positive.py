# https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        if nums == [1]:
            return 2
        else:
            i = 2
            while i < len(nums)+2:
                if i not in nums:
                    return i
                else:
                    i += 1
            