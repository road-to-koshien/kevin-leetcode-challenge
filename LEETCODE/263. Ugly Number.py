# https://leetcode.com/problems/ugly-number/

# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:

# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# Example 3:

# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num%7 == 0 or num < 0:
            return False
        result = True
        while num > 1:
            if num%2 == 0:
                num = num / 2
            if num%3 == 0:
                num = num / 3
            if num%5 == 0:
                num = num / 5
            elif num%2 != 0 and num%3 != 0 and num%5 != 0:
                break
        if num > 1:
            result = False
        return result
                