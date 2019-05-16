prices = [6,1,3,2,4,7]
print(prices)
profit = 0
raise = 0
for i in range(1, len(prices)-1):
    while prices[i] - prices[i-1] > 0:
        raise = raise + prices[i] - prices[i-1]
        continue
    

