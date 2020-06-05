## Add Two Numbers

### Problem Link

https://leetcode.com/problems/add-two-numbers/

### Problem Description 

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

```
Example 1: 

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

```

### How to solve 

**Approach 1:** 

循环遍历l1, l2, l1.val + l2.val 再加上一个进位为当前新的相加值, 如果l1或者l2为空, 将其值设置为0即可, 最后记得加进位



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0002Add_Two_Numbers/0002Add_Two_Numbers1.py)

```python
dummy = ListNode(None)
sum_node = dummy
    
carry = 0
while l1 or l2:
    if not l1:
        n1 = 0
    else:
        n1 = l1.val
        l1 = l1.next
    if not l2:
        n2 = 0
    else:
        n2 = l2.val
        l2 = l2.next
        
    sum_node.next = ListNode(None)
    sum_node = sum_node.next
    sum_node.val = (n1 + n2 + carry) % 10
    carry = (n1 + n2 + carry) // 10

print("here", carry)
if carry != 0:
    sum_node.next = ListNode(carry)
    
return dummy.next
```
