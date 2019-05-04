# https://leetcode.com/problems/valid-palindrome/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_strs = list(s)
        list_strs = list(filter(lambda x: x.isalpha() == True or x.isdigit() == True,list_strs))
        check = ''.join(list_strs).lower()
        if check[::1] == check[::-1]:
            return True
        else:
            return False