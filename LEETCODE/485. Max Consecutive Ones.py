# https://leetcode.com/problems/max-consecutive-ones/

# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m = [str(x) for x in nums]
        m = ''.join(m)
        n = m.split('0')
        max_global = 0
        for each in n:
            max_cur = len(each)
            if max_cur > max_global:
                max_global = max_cur
        return max_global
            