# https://leetcode.com/problems/to-lower-case/

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

class Solution:
    def toLowerCase(self, str: str) -> str:
        def lower_case(input_str):
            return(input_str.lower())
        return(lower_case(str))
        