# https://www.facebook.com/
# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note: N is an integer in the range [0, 10^9].

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        list_num = [int(x) for x in list(str(N))]
        while True:
            for i in range(0, len(list_num)-1):
                if list_num[i] == list_num[i+1]:
                    k = i
                    continue
                if list_num[i] > list_num[i+1]:
                    list_num[i] = list_num[i] - 1
                    for t in range(i+1, len(list_num)):
                        list_num[t] = 9
                    break
            if list_num == sorted(list_num):
                break
        res = [str(x) for x in list_num]
        res1 = int(''.join(res))
        return res1
