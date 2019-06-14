from collections import Counter
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 1
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
print(newdict)
i = 0
while i < k:
    if newdict[lists[i][0]]:
        res.append(newdict[lists[i][0]].pop())
        if len(res) == k:
            break
    else:
        i += 1
print(res)
            