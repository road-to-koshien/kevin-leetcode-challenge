strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagrams(strs):
    seen = {}
    res = []
    for i,each in enumerate(strs):
        x = sorted(each)
        x = ''.join(x)
        if x not in seen:
            seen[x] = [each]
            continue
        if x in seen:
            seen[x] = seen[x] + [each]
            continue
    print(seen)
    for i,j in seen.items():
        res.append(j)
    return res

print(groupAnagrams(strs))