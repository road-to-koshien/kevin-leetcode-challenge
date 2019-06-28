def findLongestWord(s, d):
    collect = []
    max_global = 0
    for word in d:
        t = 0
        for char in s:
            if char == word[t]:
                t += 1
                if t == len(word):
                    if len(word) == max_global:
                        collect.append(word)
                    if len(word) > max_global:
                        collect = []
                        collect.append(word)
                        max_global = len(word)
                    break
    if collect:
        collect.sort()
        return collect[0]
    else:
        return ''
s = "abpcplea"
d = ["a","b","c"]
print(findLongestWord(s,d))

