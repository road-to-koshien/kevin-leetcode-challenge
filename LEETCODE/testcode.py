from collections import Counter
nums = [4,3,2,7,8,2,3,1]
res = []
x = Counter(nums)
for i,j in x.items():
    if j == 2:
        res.append(i)
print(res)