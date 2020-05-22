## Reverse Linked List

### Problem Link
https://leetcode.com/problems/reverse-linked-list/

### Problem Description 

Reverse a singly linked list.

```
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

### How to solve 

**Method1:** 

创建一个ListNode, 和一个Temp node, 倒着指一遍


**Method2: (Iterative)** 

反指

**Method3: (Recursive)** 

Testing <sub>subscript <sub>subscript level 2</sub></sub>

The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed, now how do I reverse the front part? Let's assume the list is: n<sub>1 → … → n<sub>k - 1 → n<sub>k<sub> → n<sub>k+1<sub> → … → n<sub>m<sub> → Ø

Assume from node n<sub>k+1<sub> to nm had been reversed and you are at node nk.

n<sub>1<sub> → … → n<sub>k-1<sub> → n<sub>k<sub> → n<sub>k+1<sub> ← … ← n<sub>m<sub>

We want n<sub>k+1<sub>’s next node to point to nk.

So,

n<sub>k<sub>.next.next = n<sub>k<sub>;

Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.



### Code (python)

[My submission](https://github.com/yanray/leetcode/blob/master/problems/0206_Reverse_Linked_List/0206_Reverse_Linked_List1.py)

```python
if head is None:
    return head
else: 
    tail = temp = ListNode(head.val)
    head = head.next

    while head:
        tail = ListNode(None)
        tail.val = head.val
        head = head.next
        tail.next = temp
        temp = tail

return tail
```


[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0206_Reverse_Linked_List/0206_Reverse_Linked_List2.py)

```python
pre, cur = None, head
while cur: 
    tmp = cur
    cur  = cur.next
    tmp.next = pre
    pre = tmp
return pre
```


[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0206_Reverse_Linked_List/0206_Reverse_Linked_List3.py)

```python
prev, curr = None, head

while curr:
    curr.next, curr, prev,  = prev, curr.next, curr
return prev
```


[Method 3](https://github.com/yanray/leetcode/blob/master/problems/0206_Reverse_Linked_List/0206_Reverse_Linked_List4.py)

```python
if not head or not head.next:
    return head
n = self.reverseList(head.next)
head.next.next = head
head.next = None

return n
```