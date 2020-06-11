"""
Merge Two Sorted Lists

Version: 1.1 
Author:  Yanrui 
date:    5/21/2020
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        
        self.tail = None
        self.head = None

    def add_list_item(self, item):
        # add a node in the linked list 

        if self.head is None:
            self.head = item 
        else:
            self.tail.next = item

        self.tail = item

    def display_all_nodes(self):
        # print all values in the linked list 

        current_node = self.head

        while current_node.next is not None:
            print(current_node.val, '-> ', end = "")
            current_node = current_node.next
        print(current_node.val)


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next


if __name__ == '__main__':
    a = Solution()

    # build nodes for linked list 1
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node3 = ListNode(6)
    l1_node4 = ListNode(3)
    l1_node5 = ListNode(4)
    l1_node6 = ListNode(5)
    l1_node7 = ListNode(6)


    l1 = SingleLinkedList()
    l1.add_list_item(l1_node1)
    l1.add_list_item(l1_node2)
    l1.add_list_item(l1_node3)
    l1.add_list_item(l1_node4)
    l1.add_list_item(l1_node5)
    l1.add_list_item(l1_node6)
    l1.add_list_item(l1_node7)

    l1.display_all_nodes()

    val = 6
    new_l = a.removeElements(l1.head, val)
    l1.display_all_nodes()


