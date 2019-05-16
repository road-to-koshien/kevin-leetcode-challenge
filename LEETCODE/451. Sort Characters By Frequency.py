# https://leetcode.com/problems/sort-characters-by-frequency/

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        res = ''
        newdict = Counter(s)
        list_char = list(newdict.keys())
        char_count = list(newdict.values())
        list_char_sorted = [x for _,x in sorted(zip(char_count, list_char))]
        list_char_sorted = list_char_sorted[::-1]
        char_count.sort()
        char_count = char_count[::-1]
        for x,y in zip(list_char_sorted, char_count):
            res = res + str(x*y)
        return res