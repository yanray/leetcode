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

**Approach 2:** 

**Approach 3 - 4:** 

Recursive


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

if carry != 0:
    sum_node.next = ListNode(carry)
    
return dummy.next
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0002Add_Two_Numbers/0002Add_Two_Numbers2.py)

```python
result = head = ListNode("inf")
carry = 0
while l1 and l2:
    carry, cur = divmod(l1.val + l2.val + carry, 10)
    node = ListNode(cur)
    head.next = node
    head, l1, l2 = head.next, l1.next, l2.next
head.next = l1 if l1 else l2
while carry and head.next:
    carry, cur = divmod(head.next.val + carry, 10)
    head.next.val = cur
    head = head.next
if carry:
    head.next = ListNode(carry)
return result.next
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0002Add_Two_Numbers/0002Add_Two_Numbers3.py)

```python
def recurse(l1, l2, carry=0):
    if l1 is None and l2 is None:
        return ListNode(1) if carry == 1 else None
    
    if l1 is None:
        l1 = l2
        l2 = None
        
    if l2 is None:
        l2 = ListNode()         

    val = l1.val + l2.val + carry
    carry = val//10
    val %= 10

    return ListNode(
        val=val,
        next=recurse(l1.next, l2.next, carry)
    )

return recurse(l1, l2)
```

[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0002Add_Two_Numbers/0002Add_Two_Numbers4.py)

```python
val1 = l1 and l1.val or 0
val2 = l2 and l2.val or 0
carry, val3 = divmod(val1 + val2 + carry, 10)
node = ListNode(val3)
l1 = l1 and l1.next
l2 = l2 and l2.next
if l1 or l2 or carry:
    node.next = self.addTwoNumbers(l1, l2, carry)
return node
```