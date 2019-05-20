# https://leetcode.com/problems/reverse-linked-list/

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        list_nodes = []
        cur_node = head
        if not head:
            return []
        while cur_node:
            data = cur_node.val
            list_nodes.append(data)
            cur_node = cur_node.next
        list_nodes = list_nodes[::-1]
        head = ListNode(list_nodes[0])
        cur_node = head
        for i in range(1, len(list_nodes)):
            cur_node.next = ListNode(list_nodes[i])
            cur_node = cur_node.next
        return head
            