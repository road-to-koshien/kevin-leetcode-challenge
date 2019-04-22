# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        opened = "([{"
        closed = ")]}"
        stack = []
        balanced = True
        i = 0
        if len(s) == 1:
            return False
        while balanced and i < len(s)-1:
            for each in s:
                if each in opened:
                    stack.append(each)
                    i += 1
                else:
                    if len(stack) == 0:
                        balanced = False
                        break
                    x = stack.pop(len(stack)-1)
                    if closed.index(each) == opened.index(x):
                        i += 1
                        continue
                    else:
                        balanced = False
                        break
        if len(stack) == 0 and balanced == True:
            return True
        else:
            return False