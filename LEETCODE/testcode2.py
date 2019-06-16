def checkword(word, pattern):
    if len(word) != len(pattern):
        return False
    newdict = {}
    for i,each in enumerate(pattern):
        if each not in newdict:
            newdict[each] = word[i]
        else:
            if newdict[each] != word[i]:
                return False
            else:
                continue
    if len(set(list(pattern))) != len(set(newdict.values())):
        return False
    return True
res = []
words = ["cba","xyx","yxx","yyx"]
pattern = 'abc'
for each in words:
    if not checkword(each, pattern):
        continue
    else:
        res.append(each)
print(res)
                