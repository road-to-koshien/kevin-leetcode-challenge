# https://leetcode.com/problems/remove-linked-list-elements/

# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur_node = dummy
        while cur_node.next != None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy.next