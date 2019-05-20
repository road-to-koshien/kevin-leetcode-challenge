# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return []
        newdict = {}
        cur_node = head
        newdict[cur_node.val] = 1
        last_node = cur_node
        while cur_node and cur_node.next:
            last_node = cur_node
            data = cur_node.next.val
            if data in newdict:
                cur_node.next = cur_node.next.next
                cur_node = cur_node.next
            if data not in newdict:
                newdict[data] = 1
                cur_node = cur_node.next
        if last_node.val in newdict:
            last_node.next = None
        if last_node.val not in newdict:
        return head
                