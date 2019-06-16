def customSortString(S, T):
    need = []
    for each in S:
        while each in T:
            need.append(each)
            T = T.replace(each, '', 1)
        if each not in T:
            continue
    return ''.join(need) + T

S = "cba"
T = "abcd"
print(customSortString(S,T))