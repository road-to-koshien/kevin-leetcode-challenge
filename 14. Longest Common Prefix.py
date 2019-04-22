# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 1
        list_check = []
        final = []
        found = True
        if len(strs) == 0:
            return('')
        if len(set(strs)) == 1:
            return(strs[0])
        while found:
            for each in strs:
                list_check.append(each[0:i])
            if len(set(list_check)) == 1 and len(list_check) == len(strs):
                i += 1
                final = list_check
                list_check = []
                continue
            else:
                found = False
        if len(set(final)) == 1:
            return(final[0])
        else:
            return('')
