A = [-6,2,-6,4,-3,8,3,2,-2,6,1,-3,-4,-4,-8,4]
newdict = {}
for each in A:
    if each in newdict:
        newdict[each] = newdict[each] + 1
    if each not in newdict:
        newdict[each] = 1
print(newdict)
for each in list(newdict.keys()):
    x = 2 * each
    y = int(each/2)
    if x not in newdict and y not in newdict:
        print(False)
    elif x in newdict:
        if newdict[x] >= newdict[each]:
            newdict[x] = newdict[x] - newdict[each]
            newdict[each] = 0
        else:
            newdict[each] = newdict[each] - newdict[x]
            newdict[x] = 0
    elif y in newdict:
        if newdict[y] >= newdict[each]:
            newdict[y] = newdict[y] - newdict[each]
            newdict[each] = 0
        else:
            newdict[each] = newdict[each] - newdict[y]
            newdict[y] = 0
check = list(set(newdict.values()))
print(check)
if check != [0]:
    print(False)
else:
    print(True)

