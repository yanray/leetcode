## Intersection of Two Linked Lists

### Problem Link

https://leetcode.com/problems/intersection-of-two-linked-lists/

### Problem Description 

Click the link: https://leetcode.com/problems/intersection-of-two-linked-lists/

### How to solve 

**Approach 1:**

判断长度, 解决长度不等的问题, 判断node是否相等

**Approach 2:**

Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.

* Complexity Analysis

    - Time complexity : O(m+n)O(m+n).

    - Space complexity : O(m)O(m) or O(n)O(n).

**Approach 3:**



### Code (python)

[Approach 1]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        len_A = 0
        node_A = headA
        while node_A.next:
            node_A = node_A.next
            len_A += 1
            
        len_B = 0
        node_B = headB
        while node_B.next:
            node_B = node_B.next
            len_B += 1
            
        if node_A.val != node_B.val:
            return None
        
        node_A = headA
        node_B = headB
        if len_A > len_B:
            for _ in range(len_A - len_B):
                node_A = node_A.next
        elif len_A < len_B:
            for _ in range(len_B - len_A):
                node_B = node_B.next
                
        while node_A != node_B:
            node_A = node_A.next
            node_B = node_B.next
        
        return node_A
```

[Approach 2]

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dictA={}
        # step 1: travel headA, and storaged each node in a dict
        while headA:
            dictA[headA] = 0
            headA = headA.next
        # step 2: travel headB, check each node if in dict 
        while headB:
            # if checked, return the headB node = intersctionNode
            if headB in dictA:
                return headB
            headB = headB.next
        #No checked, no found intersctionNode
        return None
```


[Approach 3]

```python

```