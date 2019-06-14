# https://leetcode.com/problems/top-k-frequent-words/

# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        x = Counter(words)
        res = []
        newdict = {}
        lists = sorted((j,i) for (i,j) in x.items())
        lists.reverse()
        for i in range(0, len(lists)):
            newdict.setdefault(lists[i][0], []).append(lists[i][1])
        for i,j in newdict.items():
            if len(j) > 1:
                newdict[i] = sorted(j)[::-1]
        i = 0
        while i < k:
            if newdict[lists[i][0]]:
                res.append(newdict[lists[i][0]].pop())
                if len(res) == k:
                    break
            else:
                i += 1
        return(res)
            