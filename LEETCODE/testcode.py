# list1 = ['a','b','c']
# list2 = ['b','c','d']
# dict1 = dict.fromkeys(list1, 1)
# dict2 = dict.fromkeys(list2, 1)
# # dict1 &= dict2
# t = list(dict1.elements())
# print(t)
from collections import Counter
a = 'hahuythap'
t = Counter(a)
res = list(t.elements())
print(res)
print(t)