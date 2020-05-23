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

**Method1:(HashSet)** 

不断的查找Next Value, 直到最终结果为1 或者进入一个cycle

HashSet takes O(1) time

The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder.

**Method2: (Recursive)** 



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


[Method 1](https://github.com/yanray/leetcode/blob/master/problems/0202_Happy_Number/0202_Happy_Number2.py)

```python
def get_next_num(n):
    n_sum = 0
    while n != 0:
        n, mod = divmod(n, 10)
        n_sum += mod ** 2
    return n_sum

seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = get_next_num(n)
    
return n == 1
```


[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0202_Happy_Number/0202_Happy_Number3.py)

```python
prev, curr = None, head

while curr:
    curr.next, curr, prev,  = prev, curr.next, curr
return prev
```
