# https://leetcode.com/problems/uncommon-words-from-two-sentences/

# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Return a list of all uncommon words. 

# You may return the list in any order.

 

# Example 1:

# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
 

# Note:

# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        result = []
        list_del = []
        list_a = A.split()
        list_b = B.split()
        list_c = list_a + list_b
        for each in list_c:
            if list_c.count(each) == 1:
                result.append(each)
        return result