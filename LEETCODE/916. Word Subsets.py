# https://leetcode.com/problems/word-subsets/

# We are given two arrays A and B of words.  Each word is a string of lowercase letters.

# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

# Now say a word a from A is universal if for every b in B, b is a subset of a. 

# Return a list of all universal words in A.  You can return the words in any order.

# Example 1:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# Example 3:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# Example 4:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# Example 5:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
 
# Note:

# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def checkword(listdict, strs):
            for each in listdict:
                if strs.count(each[0]) < each[1]:
                    return False
            return True
        res = []
        newdict = {}
        for each in B:
            for letter in each:
                if letter in newdict:
                    newdict[letter] = max(each.count(letter), newdict[letter])
                if letter not in newdict:
                    newdict[letter] = each.count(letter)
        listdict = list(newdict.items())
        for each in A:
            if checkword(listdict, each) == True:
                res.append(each)
        return res