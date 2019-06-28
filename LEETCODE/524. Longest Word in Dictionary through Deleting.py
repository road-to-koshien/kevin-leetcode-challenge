# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]

# Output: 
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]

# Output: 
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        collect = []
        max_global = 0
        for word in d:
            t = 0
            for char in s:
                if char == word[t]:
                    t += 1
                    if t == len(word):
                        if len(word) == max_global:
                            collect.append(word)
                        if len(word) > max_global:
                            collect = []
                            collect.append(word)
                            max_global = len(word)
                        break
        if collect:
            collect.sort()
            return collect[0]
        else:
            return ''