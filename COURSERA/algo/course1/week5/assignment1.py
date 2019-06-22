#Uses Python3
def get_min_coin(coins):
    nums_coin = [None] * (coins + 1)
    nums_coin[0] = 0
    list_coins = [1,3,4]
    for i in range(1, coins+1):
        nums_coin[i] = float('inf')
        for coin in list_coins:
            if i >= coin:
                temp = nums_coin[i-coin] + 1
                if temp < nums_coin[i]:
                    nums_coin[i] = temp
            else:
                break
    return nums_coin[coins]
coins = int(input())
print(get_min_coin(coins))



