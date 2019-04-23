# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s, t):
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        result = True
        i = 0
        if len(list_s) == len(list_t):
            pass
        else:
            return False
        for i in range(len(list_s)):
            if list_s[i] == list_t[i]:
                pass
            else:
                return False
        return True