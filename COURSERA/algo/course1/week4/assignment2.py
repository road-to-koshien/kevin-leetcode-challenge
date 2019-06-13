#Uses Python3
from collections import Counter
a = input()
b = input().split()
lists = [int(x) for x in b]
x = Counter(lists)
t = len(lists) // 2
found = False
for i,j in x.items():
    if j > t:
        found = True
        break
if not found:
    print(0)
else:
    print(1)

