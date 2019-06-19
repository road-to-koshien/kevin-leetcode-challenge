def longestSubstring(s, k):
    from collections import Counter
    x = Counter(s)
    failed = []
    for i,j in x.items():
        if j < k:
            failed.append(i)
    failed = set(failed)
    start_index = 0
    newdict = {}
    max_global = 0
    i = 0
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

s = "bbaaacbd"
k = 3
print(longestSubstring(s,k))


