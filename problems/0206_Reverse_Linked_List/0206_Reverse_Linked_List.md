## Reverse Linked List

### Problem Link
https://leetcode.com/problems/reverse-linked-list/

### Problem Description 

Reverse a singly linked list.

```
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

### How to solve 

**Method1:** 

创建一个ListNode, 和一个Temp node, 倒着指一遍


**Method2:** 





### Code (python)

[Method 1](https://github.com/yanray/leetcode/blob/master/problems/0206_Reverse_Linked_List/0206_Reverse_Linked_List1.py)

```python
if head is None:
    return head
else: 
    tail = temp = ListNode(head.val)
    head = head.next

    while head:
        tail = ListNode(None)
        tail.val = head.val
        head = head.next
        tail.next = temp
        temp = tail

return tail
```


[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0206_Reverse_Linked_List/0206_Reverse_Linked_List1.py)

```python
if head is None:
    return head
else: 
    tail = temp = ListNode(head.val)
    head = head.next

    while head:
        tail = ListNode(None)
        tail.val = head.val
        head = head.next
        tail.next = temp
        temp = tail

return tail
```
