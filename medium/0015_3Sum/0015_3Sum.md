## Remove Linked List Elements

### Problem Link

https://leetcode.com/problems/remove-linked-list-elements/

### Problem Description 

Remove all elements from a linked list of integers that have value val.

```
Example 1: 

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

```


### How to solve 

**Approach 1 - 2:** 

一个prev, 一个current, 遇到val就删除

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0203Remove_Linked_List_Elements/0203Remove_Linked_List_Elements1.py)

```python
if not head:
    return head

while head.val == val:
    head = head.next
    if not head:
        return head

prev = head
curr = head.next
while curr:
    if curr.val == val:
        prev.next = curr.next
        curr = curr.next
    else:
        prev, curr = curr, curr.next
        
return head
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0203Remove_Linked_List_Elements/0203Remove_Linked_List_Elements2.py)

```python
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
```