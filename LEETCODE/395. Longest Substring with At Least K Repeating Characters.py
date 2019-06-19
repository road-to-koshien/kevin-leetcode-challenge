# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

class Solution(object):
    def longestSubstring(self, s, k):
        from collections import Counter
        x = Counter(s)
        failed = []
        for i,j in x.items():
            if j < k:
                failed.append(i)
        failed = set(failed)
        start_index,max_global,i = 0,0,0
        newdict = {}
        while i < len(s): 
            if s[i] in failed:
                if newdict and min(list(newdict.values())) < k:
                    for i in range(start_index, i):
                        check = s[start_index:i]
                        m = Counter(check)
                        if not newdict or start_index == i:
                            break
                        if min(list(m.values())) >= k: 
                            max_cur = i - start_index
                            if max_cur > max_global:
                                max_global = max_cur
                            break
                        else:
                            start_index += 1
                i += 1
                start_index = i
                newdict = {}
                continue
            if s[i] in newdict:
                newdict[s[i]] += 1
                i += 1
            else:
                if s[i] not in newdict:
                    newdict[s[i]] = 1
                    i += 1
            # print(newdict)
            if min(list(newdict.values())) >= k:
                max_cur = i - start_index 
                if max_cur > max_global:
                    max_global = max_cur
        return max_global