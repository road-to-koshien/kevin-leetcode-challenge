# https://leetcode.com/problems/reorder-list/

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        list_node = []
        cur_node = head
        while cur_node:
            list_node.append(cur_node)
            cur_node = cur_node.next
        k = head
        for i in range(0, len(list_node)):
            temp = k.next
            k.next = list_node[0-i-1]
            list_node[0-i-1].next = temp
            k = temp
            if i == (len(list_node)//2) - 1:
                break
        k.next = None