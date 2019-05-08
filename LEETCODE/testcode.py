import math
def calculate_sum(lists, i):
    sum = 0
    for each in lists:
        sum = sum + math.ceil(each/i)
    return sum
piles = [3,6,7,11]
H = 8

piles.sort()
for i, each in enumerate(piles):
    if calculate_sum(piles, each) <= H:
        t = i - 1
        break
min_x = piles[t]
max_x = piles[t+1]
if min_x > max_x:
    min_x = 1 
    max_x = piles[0]
if calculate_sum(piles, max_x) == H:
    print(max_x)
if calculate_sum(piles, min_x) == H:
    print(min_x)
else:
    x = (min_x + max_x) / 2
    while calculate_sum(piles, x) != H:
        if calculate_sum(piles, x ) > H:
            min_x = x
        if calculate_sum(piles, x) < H:
            max_x = x
        x = (min_x + max_x) / 2
print(x)
m = math.ceil(x)
n = math.floor(x)
print(m, n)
if calculate_sum(piles, n) >= H:
    print(n)
else:
    print(m)
        







