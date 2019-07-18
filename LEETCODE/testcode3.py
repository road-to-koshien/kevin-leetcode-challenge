# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
 

# Constraints:

# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.

from collections import Counter
def relativeSortArray(arr1, arr2):
    res1 = []
    res2 = []
    x = Counter(arr1)
    y = Counter(arr2)
    for each in arr2:
        if each in x:
            res1 = res1 + [each]*x[each]
        else:
            continue
    for each in arr1:
        if each in y:
            continue
        else:
            res2.append(each)
    res2.sort()
    res = res1 + res2
    return res

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(relativeSortArray(arr1, arr2))
    
[22,28,8,6,17,44]