# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i <= len(nums)-3:
            if nums[i] - nums[i+1] == 0:
                i += 2
                continue
            else:
                final = nums[i]
                break
        if i == len(nums)-1:
            final = nums[i]
        return(final)