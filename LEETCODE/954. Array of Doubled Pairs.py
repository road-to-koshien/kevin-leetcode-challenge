# https://leetcode.com/problems/array-of-doubled-pairs/
# Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

# Example 1:

# Input: [3,1,3,6]
# Output: false
# Example 2:

# Input: [2,1,2,6]
# Output: false
# Example 3:

# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
# Example 4:

# Input: [1,2,4,16,8,4]
# Output: false
 
# Note:

# 0 <= A.length <= 30000
# A.length is even
# -100000 <= A[i] <= 100000

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        newdict = {}
        if not A:
            return True
        for each in A:
            if each in newdict:
                newdict[each] = newdict[each] + 1
            if each not in newdict:
                newdict[each] = 1
        for each in list(newdict.keys()):
            x = 2 * each
            y = int(each/2)
            if x not in newdict and y not in newdict:
                return False
            elif x in newdict:
                if newdict[x] >= newdict[each]:
                    newdict[x] = newdict[x] - newdict[each]
                    newdict[each] = 0
                else:
                    newdict[each] = newdict[each] - newdict[x]
                    newdict[x] = 0
            elif y in newdict:
                if newdict[y] >= newdict[each]:
                    newdict[y] = newdict[y] - newdict[each]
                    newdict[each] = 0
                else:
                    newdict[each] = newdict[each] - newdict[y]
                    newdict[y] = 0
        check = list(set(newdict.values()))
        if check != [0]:
            return False
        else:
            return True


    
        
        
        