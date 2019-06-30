# https://leetcode.com/problems/degree-of-an-array/

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        x = Counter(nums)
        max_global = -float('inf')
        collect = []
        for i,j in x.items():
            if j == max_global:
                collect.append(i)
            elif j > max_global:
                collect = []
                collect.append(i)
                max_global = j
        min_global = float('inf')
        for each in collect:
            start = nums.index(each)
            end = nums[::-1].index(each)
            min_cur = len(nums) - end - start
            if min_cur < min_global:
                min_global = min_cur
        return min_global