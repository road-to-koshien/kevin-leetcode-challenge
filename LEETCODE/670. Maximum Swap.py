# https://leetcode.com/problems/maximum-swap/

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        list_num = [int(x) for x in list(str(num))]
        list_sorted = sorted(list_num)
        list_sorted = list_sorted[::-1]
        for i in range(0, len(list_num)):
            if list_num[i] != list_sorted[i]:
                t = list_sorted[i]
                k = str(num).rindex(str(t))
                list_num[i], list_num[k] = list_num[k], list_num[i]
                break
        res = [str(x) for x in list_num]
        res1 = int(''.join(res))
        return res1 
        

