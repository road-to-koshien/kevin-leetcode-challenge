queries = [[1,0],[-3,1],[-4,0],[2,3]]
newdict = {}
for each in queries:
    if each[1] in newdict:
        newdict[each[1]] = newdict[1] + each[0]
    if each[1] not in newdict:
        newdict[each[1]] = each[0]
print(list(newdict.items()))


1 2 3 4 5 6

0 1 2 3 4 6

