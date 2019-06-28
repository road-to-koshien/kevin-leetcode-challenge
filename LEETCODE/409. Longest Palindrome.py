# https://leetcode.com/problems/longest-palindrome/

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        x = Counter(s)
        if len(list(x.keys())) == 1:
            return len(s)
        count = 0
        for i,j in x.items():
            if j >= 2 and j%2 == 0:
                count += j
            if j >= 2 and j%2 == 1:
                found = True
                count += j -1
        if count == len(s):
            return count
        else:
            return count + 1
            