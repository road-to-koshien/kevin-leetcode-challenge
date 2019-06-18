def characterReplacement(s, k):
    newdict = {}
    max_global = 0
    i = 0
    start_index = 0
    while i < len(s):
        if s[i] in newdict:
            newdict[s[i]] += 1
        if s[i] not in newdict:
            newdict[s[i]] = 1
        count = sum(list(newdict.values())) - max(list(newdict.values()))
        print(count)
        if count > k:
            max_cur = i - start_index
            if max_cur > max_global:
                max_global = max_cur
            newdict[s[start_index]] = newdict[s[start_index]] - 1
            start_index += 1
        i += 1
        if i == len(s):
            return max((i-start_index), max_global)

s = "ABAA" #"AABAABB"
k = 0
print(characterReplacement(s,k))

