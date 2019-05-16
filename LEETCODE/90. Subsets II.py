# https://leetcode.com/problems/subsets-ii/

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new = [[num]+i for i in res]
            for each in new:
                each.sort()
                if each not in res:
                    res.append(each)
        return res
        