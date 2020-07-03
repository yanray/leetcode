## Remove Duplicates from Sorted List

### Problem Link

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

### Problem Description 

Given a sorted linked list, delete all duplicates such that each element appear only once.

```
Example 1:

Input: 1->1->2
Output: 1->2

```

```
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

```


### Code (python)

[Approach 1] (98%)

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        seen = set()
        prev = head
        dummy = head.next
        seen.add(prev.val)
        while dummy:
            if dummy.val in seen:
                dummy = dummy.next
                prev.next = dummy
            else:
                seen.add(dummy.val)
                dummy = dummy.next
                prev = prev.next
            
        return head
```

[Approach 2] (>>66%)

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None : return head
        prev = temp = head
        while(temp.next != None):
            if temp.val != temp.next.val : prev.next = temp.next ; prev = temp.next
            temp = temp.next
        prev.next = None
        return head
```

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        st=head
        while head:
            while(head.next and head.val==head.next.val):
                head.next=head.next.next
            head=head.next
        
        
        return(st)
```

https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/502590/RECURSIVE-SOLUTION-greater-for-concept-building

