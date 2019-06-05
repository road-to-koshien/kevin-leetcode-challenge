# https://leetcode.com/problems/longest-harmonious-subsequence/

# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.

class Solution(object):
    def findLHS(self, nums):
        from collections import Counter
        x = Counter(nums)
        max_global = 0
        for each in x.keys():
            if each+1 not in x:
                continue
            if each+1 in x:
                max_cur = x[each] + x[each+1]
                if max_cur > max_global:
                    max_global = max_cur
        return max_global
        