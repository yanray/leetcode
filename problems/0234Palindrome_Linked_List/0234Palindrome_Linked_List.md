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


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0234Palindrome_Linked_List/0234Palindrome_Linked_List1.py)

```python
cs_sequence = ["0", "1"]

for i in range(1, n):
    prev_cs_str = cs_sequence[i]
    
    cs_str = ""
    num_count = 0
    for j, ch in enumerate(prev_cs_str):
        if (j + 1) == len(prev_cs_str) or prev_cs_str[j + 1] != ch:
            cs_str += str(num_count + 1) + ch
            num_count = 0
        elif prev_cs_str[j + 1] == ch:
            num_count += 1

    cs_sequence.append(cs_str)
    
return cs_sequence[n]
```
