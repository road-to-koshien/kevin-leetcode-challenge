# https://leetcode.com/problems/length-of-last-word/
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0 or set(s) == {' '}:
            return 0
        if len(s) == 1:
            return 1
        b = s.split()
        return(len(b[-1]))
        