"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/22/2020
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
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            curr.next, curr, prev,  = prev, curr.next, curr
        return prev
            


if __name__ == '__main__':
    a = Solution()

    # build nodes for linked list 1
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node3 = ListNode(3)
    l1_node4 = ListNode(4)
    l1_node5 = ListNode(5)


    l1 = SingleLinkedList()
    l1.add_list_item(l1_node1)
    l1.add_list_item(l1_node2)
    l1.add_list_item(l1_node3)
    l1.add_list_item(l1_node4)
    l1.add_list_item(l1_node5)


    # display l1, l2
    l1.display_all_nodes()

    reversed_l1 = a.reverseList(l1.head)

    # To display reversed_l1
    display_newl = reversed_l1
    while display_newl.next is not None:
        print(display_newl.val, '-> ', end = "")
        display_newl = display_newl.next
    print(display_newl.val)


    


