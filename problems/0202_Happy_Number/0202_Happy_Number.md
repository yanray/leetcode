## Happy Number

### Problem Link
https://leetcode.com/problems/happy-number/

**Python Set**
https://docs.python.org/2/library/sets.html

### Problem Description 

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

```
Example:

Input: 19
Output: true
```
Explanation: 

1<sup>2</sup> + 9<sup>2</sup> = 82

8<sup>2</sup> + 2<sup>2</sup> = 68

6<sup>2</sup> + 8<sup>2</sup> = 100

1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1

### How to solve 

**Method1:** 

不断的查找Next Value, 直到最终结果为1 或者进入一个cycle

HashSet takes O(1) time

The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder.

**Method3: (Recursive)** 



### Code (python)

[My submission](https://github.com/yanray/leetcode/blob/master/problems/0202_Happy_Number/0202_Happy_Number1.py)

```python
before_nums = []
n_sum = n

while n_sum != 1: 
    n = n_sum
    n_sum = 0

    if n in before_nums:
        return False

    before_nums.append(n)
    while n >= 1:
        n_sum = n_sum + pow(n % 10, 2)
        n = int(n / 10)
    
return True
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