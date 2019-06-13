#Uses Python3
def binary_search(array, x):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        if array[mid] < x:
            low = mid + 1
        if array[mid] > x:
            high = mid - 1
    return -1
input1 = input().split()
input2 = input().split()
list1 = [int(input1[i]) for i in range(1, len(input1))]
list2 = [int(input2[i]) for i in range(1, len(input2))]
res = []
newdict = {}
for each in list2:
    if each not in newdict:
        result = binary_search(list1, each)
        newdict[each] = result
        res.append(result)
    else:
        res.append(newdict[each])
for each in res:
    print(each, end=' ')


