## Valid Parentheses

### Problem Link
https://leetcode.com/problems/merge-two-sorted-lists/

### Problem Description 

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


```
Example1:

**Input**: 1->2->4, 1->3->4
**Output**:  1->1->2->3->4->4

```


### How to solve 
创建一个新的Linked list, 每次判断l1和l2第一个node的值的大小，不断的插入最小的值，直到l1和l2有一个为空，再把剩下的值都加到新的linekd list

**Dynamic Programing: **
list1[0]+merge(list1[1:],list2)  if list1[0]<list2[0]
list2[0]+merge(list1,list2[1:])  otherwise

​

### Code (python)

[My Submission](https://github.com/yanray/leetcode/blob/master/problems/0021Merge_Two_Sorted%20_Lists/0021Merge_Two_Sorted%20_Lists.py)

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

[DP](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum2.py)

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
