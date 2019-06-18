# https://leetcode.com/problems/longest-repeating-character-replacement/

# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

class Solution(object):
    def characterReplacement(self, s, k):
        newdict = {}
        max_global = 0
        i = 0
        start_index = 0
        if not s:
            return 0
        while i < len(s):
            if s[i] in newdict:
                newdict[s[i]] += 1
            if s[i] not in newdict:
                newdict[s[i]] = 1
            count = sum(list(newdict.values())) - max(list(newdict.values()))
            print(count)
            if count > k:
                max_cur = i - start_index
                if max_cur > max_global:
                    max_global = max_cur
                newdict[s[start_index]] = newdict[s[start_index]] - 1
                start_index += 1
            i += 1
            if i == len(s):
                return max((i-start_index), max_global)