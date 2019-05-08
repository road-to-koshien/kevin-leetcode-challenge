# https://leetcode.com/problems/koko-eating-bananas/
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

# Return the minimum integer K such that she can eat all the bananas within H hours.

# Example 1:

# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
 
# Note:

# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def calculate_sum(lists, i):
            sum = 0
            for each in lists:
                sum = sum + math.ceil(each/i)
            return sum
        if len(piles) == 1 and piles[0] <= H:
            return 1
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
            return(max_x)
        if calculate_sum(piles, min_x) == H:
            return(min_x)
        else:
            x = (min_x + max_x) / 2
            while calculate_sum(piles, x) != H:
                if calculate_sum(piles, x ) > H:
                    min_x = x
                if calculate_sum(piles, x) < H:
                    max_x = x
                x = (min_x + max_x) / 2
        m = math.ceil(x)
        n = math.floor(x)
        if calculate_sum(piles, n) <= H:
            return n
        else:
            return m