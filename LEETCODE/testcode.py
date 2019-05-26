def k_smallest(lists, k):
    lists.sort()
    return lists[:k]

lists = [1,6,2,2,7,10]
print(k_smallest(lists, 3))