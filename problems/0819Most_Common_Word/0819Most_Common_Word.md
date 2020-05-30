## Palindrome Linked List

### Problem Link

https://leetcode.com/problems/palindrome-linked-list/

### Problem Description 

Given a singly linked list, determine if it is a palindrome.

```
Example 1: 

Input: 1->2
Output: false

```

```
Example 2: 

Input: 1->2->2->1
Output: true

```

**Follow up:**
Could you do it in O(n) time and O(1) space?

### How to solve 

**Approach 1:** 

Linked list to list 

**Approach 2:**

Use recursion


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0234Palindrome_Linked_List/0234Palindrome_Linked_List1.py)

```python
s = []
while head:
    s.append(str(head.val))
    head = head.next

return s == s[::-1]
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0234Palindrome_Linked_List/0234Palindrome_Linked_List2.py)

```python
self.front_pointer = head

def recursively_check(current_node=head):
    if current_node is not None:
        if not recursively_check(current_node.next):
            return False
        if self.front_pointer.val != current_node.val:
            return False
        self.front_pointer = self.front_pointer.next
    return True

return recursively_check()
```
