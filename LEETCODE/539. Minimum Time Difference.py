# https://leetcode.com/problems/minimum-time-difference/

# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def check_min(a,b):
            x = a.split(':')
            y = b.split(':')
            x = [int(x) for x in x]
            y = [int(x) for x in y]
            if x[0] < y[0]:
                x,y = y,x
            if (x[0] -y[0]) <= 12:
                return(abs((x[0]*60 + x[1]) - (y[0]*60 + y[1])))
            else:
                return(abs((x[0]*60 + x[1]) - ((y[0]+24)*60 + y[1])))
        check = []
        min_global = float('inf')
        for each in timePoints:
            t = each.split(':')
            t = int(t[0] + t[1])
            check.append(t)
        timePoints_sorted = [x for _,x in sorted(zip(check, timePoints))]
        timePoints_sorted = timePoints_sorted + [timePoints_sorted[0]]
        for i in range(len(timePoints_sorted)-1):
            min_cur = check_min(timePoints_sorted[i], timePoints_sorted[i+1])
            if min_cur < min_global:
                min_global = min_cur
        return(min_global)