k = 5
i = 3
a = list(range(0, k+1))


res = [[]]
final = []
for each in a:
    add = [i + [each] for i in res]
    for item in add:
        res.append(item)
        if len(item) == i:
            final.append(item)
print(final)