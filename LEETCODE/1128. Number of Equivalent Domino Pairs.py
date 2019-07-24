# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
 
# Constraints:

# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        newdict = {}
        count = 0
        for i in range(len(dominoes)):
            dominoes[i] = sorted(dominoes[i])
        for i in range(len(dominoes)):
            tmp = tuple(dominoes[i])
            if tmp in newdict:
                newdict[tmp] += 1
            else:
                newdict[tmp] = 1
        for i,j in newdict.items():
            if j == 1:
                continue
            if j == 2:
                count += 1
                continue
            if j > 2:
                count = count + int(j*(j-1)/2)
        return count
            