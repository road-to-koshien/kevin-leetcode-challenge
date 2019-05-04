nums = [2, 6, 4, 8, 10, 9, 15]
# nums = 2 4 6 8 9 10 15
nums_sort = sorted(nums)

for i in range(0, len(nums)):
    if nums[i] == nums_sort[i]:
        continue
    else:
        t = i
        break
for k in range (len(nums)-1, t , -1):
    if nums[k] == nums_sort[k]:
        continue
    else:
        m = k
        break
print(abs(m-t))

