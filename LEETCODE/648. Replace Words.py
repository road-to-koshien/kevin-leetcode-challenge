# https://leetcode.com/problems/replace-words/

# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

# You need to output the sentence after the replacement.

# Example 1:

# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
 

# Note:

# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        newdict = {}
        for each in dict:
            t = len(each)
            if t in newdict:
                newdict[t].append(each)
            if t not in newdict:
                newdict[t] = [each]
        min_dict = min(list(newdict.keys()))
        sens = sentence.split(' ')
        for i in range(0, len(sens)):
            t = len(sens[i])
            if t < min_dict:
                continue
            for k in sorted(list(newdict.keys())):
                for item in newdict[k]:
                    if sens[i].find(item) == 0:
                        sens[i] = item
                        break
                continue
        return(' '.join(sens))