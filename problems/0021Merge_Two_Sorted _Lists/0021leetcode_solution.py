"""
Merge Two Sorted Lists

Version: 1.1 
Author:  Yanrui 
date: 	 5/21/2020
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        node = dummy
        
        while l1 and l2: 
            if l1.val < l2.val:
                node.next = l1
                l1= l1.next
            else: 
                node.next = l2
                l2 = l2.next
            node = node.next
                
        if l1:
            node.next = l1
        else:
            node.next = l2
            
        return dummy.next
