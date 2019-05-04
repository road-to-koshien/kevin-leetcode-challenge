# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        if nums == nums_sort:
            return 0
        for i in range(0, len(nums)):
            if nums[i] == nums_sort[i]:
                continue
            else:
                t = i
                break
        for k in range (len(nums)-1, t , -1):
            if nums[k] == nums_sort[k]:
                continue
            else:
                m = k
                break
        return(abs(m-t)+1)