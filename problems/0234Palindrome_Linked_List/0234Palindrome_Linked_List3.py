"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/29/2020
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
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        # reverse left half of the list while searching
        # the start point of the right half
        while fast is not None and fast.next is not None:
            tmp = slow

            # keep moving guys
            slow = slow.next
            fast = fast.next.next

            # place node at the start of the reversed half
            tmp.next = reversed_list
            reversed_list = tmp

        # if there are even number of elements in the list
        # do one more step to reach the first element of
        # the second list's half
        if fast is not None:
            slow = slow.next

        # compare reversed left half with the original
        # right half
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return reversed_list is None

if __name__ == '__main__':
    a = Solution()

    # build nodes for linked list 1
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node3 = ListNode(2)
    l1_node4 = ListNode(1)


    l1 = SingleLinkedList()
    l1.add_list_item(l1_node1)
    l1.add_list_item(l1_node2)
    l1.add_list_item(l1_node3)
    l1.add_list_item(l1_node4)


    # display l1, l2
    l1.display_all_nodes()

    print(a.isPalindrome(l1.head))


    


