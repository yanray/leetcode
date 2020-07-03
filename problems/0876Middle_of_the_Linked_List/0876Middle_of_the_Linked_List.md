## Middle of the Linked List

### Problem Link

https://leetcode.com/problems/middle-of-the-linked-list/

### Problem Description 

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

```
Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

```

```
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

```

**Note:**

The number of nodes in the given list will be between 1 and 100.

### Code (python)

[Approach 1] (75%)

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
            
        return node_list[len(node_list) // 2]
```

[Approach 2: Fast and Slow Pointer] (75%)

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

```python
class Solution:
    def middleNode(self, head):
        
        def recur(slow, fast): #Recursion helper function. Called by `middleNode()` later.
            if not fast or not fast.next: #Detect if fast pointer is at the end of the linked list.
                return slow #If fast is at the end, slow pointer must be at the middle - see below.
            slow = slow.next #Will always be behind fast by a factor of two.
            fast = fast.next.next #Traverses twice as quickly as slow.
            return recur(slow, fast) #Make recursive call, no need to increment slow and fast here, done above already.
        
        return recur(head, head) #Both pointers start at the head of the linked list.
```