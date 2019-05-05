# https://leetcode.com/problems/valid-boomerang/
# A boomerang is a set of 3 points that are all distinct and not in a straight line.

# Given a list of three points in the plane, return whether these points are a boomerang.

 
# Example 1:

# Input: [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:

# Input: [[1,1],[2,2],[3,3]]
# Output: false
 
# Note:

# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100

import math
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def get_length(list_1, list_2):
            length = (list_1[0] - list_2[0])**2 + (list_1[1] - list_2[1])**2
            return math.sqrt(length)
        list_1 = points[0]    
        list_2 = points[1]
        list_3 = points[2]
        length_1 = get_length(list_1, list_2)
        length_2 = get_length(list_2, list_3)
        length_3 = get_length(list_1, list_3)
        if abs(length_1 - length_2) == length_3 or abs(length_1 - length_3) == length_2 or abs(length_2 - length_3) == length_1:
            return(False)
        else:
            return(True)

