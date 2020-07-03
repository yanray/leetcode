## Linked List Cycle

### Problem Link

https://leetcode.com/problems/linked-list-cycle/

### Problem Description 

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

```
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

```

```
Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

```

```
Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

```

**Follow up:**

Can you solve it using O(1) (i.e. constant) memory?



### Code (python)

[Approach 1] (90%)

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow:
            if slow == fast:
                return True
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return False
```

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow=head
        fast=head

        while fast!=None and fast.next!=None:

            slow=slow.next
            fast=fast.next.next

            if(slow==fast):
                return True

        return False
```

[Approach 2] (75%)

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l={}
        while head:
            if(head in l):
                return True
            else:
                l[head]=True
            head=head.next
        return False
```

[Approach 3] (60%)

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        node = head
        while True:
            if node is None:
                return False
            l = len(seen)
            seen.add(node)
            if len(seen) == l:
                return True
            node = node.next
```