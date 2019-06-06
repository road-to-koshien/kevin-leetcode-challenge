# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        from collections import Counter
        x = Counter(s)
        y = Counter(t)
        newdict = {}
        if len(s) != len(t):
            return False
        for i,each in enumerate(s):
            if x[each] == y[t[i]]:
                if each in newdict:
                    if newdict[each] != t[i]:
                        return False
                if each not in newdict:
                    newdict[each] = t[i]
                continue
            else:
                return False
        return True
        