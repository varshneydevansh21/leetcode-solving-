# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Step 1: Overwrite current node's value with the next node's value
        node.val = node.next.val
        
        # Step 2: Skip the next node by pointing to the one after it
        node.next = node.next.next