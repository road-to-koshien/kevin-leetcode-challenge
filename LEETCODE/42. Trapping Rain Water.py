# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height: List[int]) -> int:
        x= sum= sum2= k= final= final2= 0
        n = len(height)
        temp = []
        if n <=2:
            return 0
        if n == 3:
            if height[0] - height[1] > 0 and height[2] - height[1] >0:
                height.remove(max(height))
                final = abs(height[0] - height[1])
            else:
                return 0    
        else:
            while height[x] == 0:
                x += 1
            min = height[x]
            x += 1
            while x <= n-1:
                if height[x] < min:
                    sum = sum - height[x] + min
                    x += 1
                    continue
                else:
                    min = height[x]
                    k = x
                    x +=1
                    final = sum
            if x > n-1:
                x -= 1
            if k < n-1:
                while height[x] == 0:
                    x -= 1
                min = height[x]
                x -= 1
                while x >= k+1:
                    if height[x] <= min:
                        sum2 = sum2 - height[x] + min
                        if x == k+1:
                            final2 = sum2
                        x -= 1
                        continue
                    else:
                        min = height[x]
                        x -= 1
                        final2 = sum2
                if final2 == 0:
                    final2 = sum2
            final = final + final2
        return final