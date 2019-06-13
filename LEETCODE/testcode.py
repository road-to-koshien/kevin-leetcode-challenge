def isValid(s):
    from collections import Counter
    x = Counter(s)
    res = []
    for each in x.values():
        res.append(each)
    set_res = list(set(res))
    print(x)
    if len(set_res) == 1:
        return('YES')
    elif len(set_res) == 2:
        if abs(set_res[0] - set_res[1]) == 1:
            if Counter(x.values())[set_res[0]] > 1:
                if Counter(x.values())[set_res[1]] == 1:
                    return('YES')
            elif Counter(x.values())[set_res[1]] > 1:
                if Counter(x.values())[set_res[0]] == 1:
                    return('YES')
            return('NO')
        if set_res[0] == 1 and Counter(x.values())[set_res[0]] == 1:
            return('YES')
        if set_res[1] == 1 and Counter(x.values())[set_res[1]] == 1:
            return('YES')
        else:
            return('NO')
    else:
        return('NO')
x = 'aaaaabc'
print(isValid(x))


