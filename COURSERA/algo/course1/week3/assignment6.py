#Uses Python3
n = int(input())
newdict = {}
t = 1
while n != 0:
    temp = n
    n = n - t
    if n not in newdict and n != t:
        newdict[t] = 1
        t += 1
    else:
        t += 1
        n = temp
        continue
print(len(newdict.keys()))
for each in newdict.keys():
    print(each, end=' ')