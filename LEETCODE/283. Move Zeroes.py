# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        try:
            t = 1
            while nums.index(0) >= 0 and nums.index(0) < len(nums) - t:
                nums.pop(nums.index(0))
                nums.append(0)
                t += 1
        except ValueError:
            pass
        