letters = ["c","f","j"]
target = 'c'
sums = letters + [target]
sums = set(sums)
sums = list(sums)
sums.sort()
t = sums.index(target)
if t == len(sums) - 1:
    print(sums[t])
else:
    print(sums[t+1])