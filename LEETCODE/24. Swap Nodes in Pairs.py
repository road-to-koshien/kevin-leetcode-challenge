# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur_node = head
        list_nodes = []
        i = 0
        if not head:
            return []
        while cur_node:
            list_nodes.append(cur_node)
            cur_node = cur_node.next
        while i < len(list_nodes) - 1:
            list_nodes[i], list_nodes[i+1] = list_nodes[i+1], list_nodes[i]
            i += 2
        head = list_nodes[0]
        cur_node = head
        for i in range(1, len(list_nodes)):
            cur_node.next = list_nodes[i]
            cur_node = cur_node.next
        cur_node.next = None
        return head