# https://leetcode.com/problems/reorganize-string/

# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"
# Example 2:

# Input: S = "aaab"
# Output: ""
# Note:

# S will consist of lowercase letters and have length in range [1, 500].


class Solution:
    def reorganizeString(self, S: str) -> str:
        S_set = list(set(S))
        list_count = []
        for each in S_set:
            count_char = S.count(each)
            list_count.append(count_char)
        if max(list_count) >= int(len(S))/2+1:
            return('')
        else:
            S_new_set = [x for _,x in sorted(zip(list_count, S_set))]
            list_count.sort()
            S_new_set = S_new_set[::-1]
            list_count = list_count[::-1]
            res = ''
            while len(S_new_set) > 1:
                    i = 0
                    if list_count[i] >= list_count[i+1]:
                        res = res + (S_new_set[i]+S_new_set[i+1])*(list_count[i+1])
                        list_count[i] = list_count[i] - list_count[i+1]
                        list_count.pop(i+1)
                        S_new_set.pop(i+1)
                    else:
                        res = res + (S_new_set[i+1]+S_new_set[i])*(list_count[i])
                        list_count[i+1] = list_count[i+1] - list_count[i]
                        list_count.pop(i)
                        S_new_set.pop(i)
        res = list(res)
        x = list_count[0]
        y = S_new_set[0]
        if x == 0:
            res = ''.join(res)
            return res
        if x == 1:
            res = res + [y]
            res = ''.join(res)
            return res
        else:
            for i in range(0, 2*x, 2):
                res.insert(i, y)
                x = x - 1
                if x == 0:
                    break
            res = ''.join(res)
            return res
