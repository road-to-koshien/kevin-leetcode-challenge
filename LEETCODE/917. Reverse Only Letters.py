# https://leetcode.com/problems/reverse-only-letters/

# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 
# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        i, j = 0, -1
        while i + abs(j) <= len(S)-1:
            if S[i].isalpha() == True and S[j].isalpha() == True:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
                continue
            if S[i].isalpha() == False and S[j].isalpha() == False:
                i += 1
                j -= 1
                continue
            if S[i].isalpha() == True and S[j].isalpha() == False:
                j -= 1
                continue
            if S[i].isalpha() == False and S[j].isalpha() == True:
                i += 1
                continue
        S = ''.join(S)
        return S