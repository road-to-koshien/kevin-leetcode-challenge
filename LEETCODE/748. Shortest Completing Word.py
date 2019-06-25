# https://leetcode.com/problems/shortest-completing-word/

# Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

# Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

# The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
# Output: "steps"
# Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the word twice.
# Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
# Output: "pest"
# Explanation: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.
# Note:
# licensePlate will be a string with length in range [1, 7].
# licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range [1, 15].


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        newdict = {}
        for char in licensePlate:
            if char.isalpha() == False:
                continue
            if char.isupper() == True:
                char = char.lower()
            if char in newdict:
                newdict[char] += 1
            if char not in newdict:
                newdict[char] = 1
        
        length = len(newdict.keys())
        found = True
        min_global = float('inf')
        for word in words:
            if len(word) > min_global:
                continue
            else:
                count = 0
                found = True
                check = Counter(word)
                for each in check.keys():
                    if each not in newdict:
                        continue
                    elif each in newdict:
                        if check[each] < newdict[each]:
                            found = False
                            break
                        else:
                            count += 1
                            continue
                if found and count == length:
                    min_cur = len(word)
                    if min_cur < min_global:
                        min_global = min_cur
                        res = word
        return res