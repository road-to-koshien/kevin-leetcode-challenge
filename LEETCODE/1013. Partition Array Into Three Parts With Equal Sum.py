# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

# Example 1:

# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# Example 3:

# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
# Note:

# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000

class Solution(object):
    def canThreePartsEqualSum(self, A):
        sums = sum(A)
        equal = sums / 3
        sum_temp = 0
        count = 0
        for each in A:
            sum_temp = sum_temp + each
            if sum_temp != equal:
                continue
            else:
                count += 1
                sum_temp = 0
        if count == 3:
            return True
        else:
            return False