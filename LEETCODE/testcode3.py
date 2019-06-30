def findShortestSubArray(nums):
    from collections import Counter
    x = Counter(nums)
    max_global = -float('inf')
    collect = []
    for i,j in x.items():
        if j == max_global:
            collect.append(i)
        elif j > max_global:
            collect = []
            collect.append(i)
            max_global = j
    print(collect)
    min_global = float('inf')
    for each in collect:
        start = nums.index(each)
        end = nums[::-1].index(each)
        min_cur = len(nums) - end - start
        if min_cur < min_global:
            min_global = min_cur
    return min_global

nums = [1,1,2,2,2,1]
print(findShortestSubArray(nums))
                