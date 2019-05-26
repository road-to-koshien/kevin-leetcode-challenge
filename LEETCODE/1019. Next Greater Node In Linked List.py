# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        lists,stack = [],[]
        cur_node = head
        while cur_node:
            lists.append(cur_node.val)
            cur_node = cur_node.next
        res = [0] * len(lists)
        for i in range(0, len(lists)):
            while stack and lists[i] > lists[stack[-1]]:
                res[stack.pop()] = lists[i]
            stack.append(i)
        return res
            