# https://leetcode.com/problems/group-anagrams/

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution(object):
    def groupAnagrams(self, strs):
        seen = {}
        res = []
        for i,each in enumerate(strs):
            x = sorted(each)
            x = ''.join(x)
            if x not in seen:
                seen[x] = [each]
                continue
            if x in seen:
                seen[x] = seen[x] + [each]
                continue
        for i,j in seen.items():
            res.append(j)
        return res
            