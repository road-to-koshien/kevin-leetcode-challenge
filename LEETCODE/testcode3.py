nums = [1,2,3,4]
nums.sort(reverse = True)
list_multi = nums[:3]
res = 1
for each in list_multi:
    res = res * each
print(res)