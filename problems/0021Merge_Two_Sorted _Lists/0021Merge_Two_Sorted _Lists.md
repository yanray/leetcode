## Merge Two Sorted Lists

### Problem Link
https://leetcode.com/problems/merge-two-sorted-lists/

### Problem Description 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


```
Example1:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

```


### How to solve 


​

### Code (python)

[My Submission](https://github.com/yanray/leetcode/blob/master/problems/0021Merge_Two_Sorted%20_Lists/0021Merge_Two_Sorted%20_Lists1.py)

```python
dummy = ListNode(None)
node = dummy

while l1 and l2: 
    if l1.val < l2.val:
        node.next = l1
        l1= l1.next
    else: 
        node.next = l2
        l2 = l2.next
    node = node.next
        
if l1:
    node.next = l1
else:
    node.next = l2
    
return dummy.next
```

[Dynamic Programing](https://github.com/yanray/leetcode/blob/master/problems/0021Merge_Two_Sorted%20_Lists/0021Merge_Two_Sorted%20_Lists2.py)

```python
if l1 is None:
    return l2
elif l2 is None:
    return l1
elif l1.val < l2.val:
    l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
else:
    l2.next = self.mergeTwoLists(l1, l2.next)
    return l2
```
