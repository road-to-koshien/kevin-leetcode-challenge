from collections import Counter
nums = [3,3,7,7,10,11,11]
count = Counter(nums)
print(count)
res = list(count.keys())[list(count.values()).index(1)]
print(res)