a = "AABAACAADAABAABA"
b = 'AABA'
res = []
for i in range(len(a)):
    t = 0
    k = i
    while a[k] == b[t]:
        k += 1
        if t == len(b) - 1:
            res.append(i)
            break
        t += 1
print(res)  

