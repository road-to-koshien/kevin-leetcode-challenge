from collections import Counter
s = 'hahuythap'
b = Counter(s)
x = list(b.keys())
y = list(b.values())
print(x, y)

new_list = [x for _,x in sorted(zip(y, x))]
print(new_list)
