"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(None)
        sum_node = dummy
            
        carry = 0
        while l1 or l2:
            if not l1:
                n1 = 0
            else:
                n1 = l1.val
                l1 = l1.next
            if not l2:
                n2 = 0
            else:
                n2 = l2.val
                l2 = l2.next
                
            sum_node.next = ListNode(None)
            sum_node = sum_node.next
            sum_node.val = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
        
        if carry != 0:
            sum_node.next = ListNode(carry)
            
        return dummy.next


if __name__ == '__main__':
    a = Solution()

    # build nodes for linked list 1
    l1_node1 = ListNode(2)
    l1_node2 = ListNode(4)
    l1_node3 = ListNode(3)


    l1 = SingleLinkedList()
    l1.add_list_item(l1_node1)
    l1.add_list_item(l1_node2)
    l1.add_list_item(l1_node3)

    # build nodes for linked list 2
    l2_node1 = ListNode(5)
    l2_node2 = ListNode(6)
    l2_node3 = ListNode(4)


    l2 = SingleLinkedList()
    l2.add_list_item(l2_node1)
    l2.add_list_item(l2_node2)
    l2.add_list_item(l2_node3)


    # display l1, l2
    l1.display_all_nodes()
    l2.display_all_nodes()

    new_l = a.addTwoNumbers(l1.head, l2.head)

    display_newl =new_l
    while display_newl.next is not None:
        print(display_newl.val, '-> ', end = "")
        display_newl = display_newl.next
    print(display_newl.val)

    
