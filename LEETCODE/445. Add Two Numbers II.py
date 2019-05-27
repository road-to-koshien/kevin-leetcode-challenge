# https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res1, res2 = [], []
        while l1:
            res1.append(l1.val)
            l1 = l1.next
        while l2:
            res2.append(l2.val)
            l2 = l2.next
        res1 = [str(x) for x in res1]
        res1 = int(''.join(res1))
        res2 = [str(x) for x in res2]
        res2 = int(''.join(res2))
        res3 = str(res1 + res2)
        head = ListNode(0)
        k = head
        for i in range(len(res3)):
            k.next = ListNode(int(res3[i]))
            k = k.next
        return head.next
        