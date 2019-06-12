#Uses Python3
def binary_search(array, low, high, k):
    mid = (low + high) // 2
    if low > high:
        return -1
    if array[mid] > k:
        high -= 1
        return binary_search(array, low, high, k)
    if array[mid] < k:
        low += 1
        return binary_search(array, low, high, k)
    if array[mid] == k:
        return mid
input1 = input().split()
input2 = input().split()
list1 = [int(input1[i]) for i in range(1, len(input1))]
list2 = [int(input2[i]) for i in range(1, len(input2))]
res = []
low = 0
high = len(list1) - 1
for each in list2:
    res.append(binary_search(list1, low, high, each))
if list2 == []:
    
for each in res:
    print(each, end=' ')


