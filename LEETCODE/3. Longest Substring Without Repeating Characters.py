# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string = ''
        max_length = 0
        for i in range(len(s)):
            if max_string.find(s[i]) == -1:
                max_string = max_string + s[i]
                if len(max_string) > max_length:
                    max_length = len(max_string)
            else:
                max_string = max_string + s[i]
                t = max_string.find(s[i]) + 1
                max_string = max_string[t:]
        return(max_length)
    