# https://leetcode.com/problems/maximum-width-ramp/

# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

# Example 1:

# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
# Example 2:

# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

# Note:

# 2 <= A.length <= 50000
# 0 <= A[i] <= 50000

class Solution(object):
    def maxWidthRamp(self, A):
        list_index = []
        for i,each in enumerate(A):
            list_index.append(i)
        list_check = [x for _,x in sorted(zip(A,list_index))]
        max_current = 0
        i_min = float('inf')
        for each in list_check:
            max_current = max(max_current, each - i_min)
            i_min = min(each, i_min)
        return max_current