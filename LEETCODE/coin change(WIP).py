# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

A = "s z z z s"
B = "s z ejt"

result = []
list_del = []
list_a = A.split()
list_b = B.split()
list_aset = list(set(list_a))
list_bset = list(set(list_b))
print(list_a.count('s'))
for each in list_aset:
    if list_a.count(each) > 1:
        list_aset.remove(each)
    continue
print(list_aset)
for each in list_bset:
    if list_b.count(each) > 1:
        list_bset.remove(each)
for each in list_aset:
    if each in list_bset:
        list_del.append(each)
for each in list_del:
    list_aset.remove(each)
    list_bset.remove(each)
result = list_aset + list_bset


