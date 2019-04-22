# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

class Solution:
    def reverse(self, x):
        s = list(str(x))
        s.reverse()
        if s[0] == 0:
            s.pop(0)
        if s[-1] == '-':
            s.pop(-1)
            s.insert(0, '-')
        num = ''.join(s)
        num = int(num)
        if num < -2**31:
            return 0
        if num > 2**31 -1:
            return 0
        return num