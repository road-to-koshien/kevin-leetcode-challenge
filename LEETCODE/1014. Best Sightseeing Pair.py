# https://leetcode.com/problems/best-sightseeing-pair/

# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

# Example 1:

# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

# Note:

# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        max1 = 0
        res = 0
        for i, each in enumerate(A):
            res_cur = max1 + each - i
            if res_cur > res:
                res = res_cur
            max_cur = A[i] + i
            if max_cur > max1:
                max1 = max_cur
        return(res)