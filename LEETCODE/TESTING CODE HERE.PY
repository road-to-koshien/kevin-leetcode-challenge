def check_thap(nums, k):
    newdict = {}
    result = False
    for i, each in enumerate(nums):
        if each in newdict:
            for item in newdict[each]:
                if i - item <= k:
                    result = True       
            newdict[each].append(i)
        if each not in newdict:
            newdict[each] = [i]
    return result

a = [1,2,3,1,2,3]
b = 2
print(check_thap(a, b))
# a = {}
# a[1] = [5]
# print(a[1])
# a[1].append(6)
# print(a)
# temp = check_thap(a,b)
# for each in temp[1]:
#     print(each)