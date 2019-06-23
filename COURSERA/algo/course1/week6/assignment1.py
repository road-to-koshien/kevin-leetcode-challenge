# Uses python3
import sys
def optimal_weight(W, w):
    dp_result = [[0 for x in range(W + 1)] for y in range(n + 1)]
    for i in range(1, n+1):
        for weight in range(1, W+1):
            dp_result[i][weight] = dp_result[i-1][weight]
            if w[i-1] <= weight:
                val = dp_result[i-1][weight - w[i-1]] + w[i-1]
                if val > dp_result[i][weight]:
                    dp_result[i][weight] = val
    return dp_result[n][W]
capacity = input().split()
list_gold = input().split()
W = int(capacity[0])
w = [int(x) for x in list_gold]
n = len(w)
print(optimal_weight(W,w))