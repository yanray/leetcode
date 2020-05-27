## Single Number

### Problem Link
https://leetcode.com/problems/single-number/

### Problem Description 

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```
Example 1:

Input: [2,2,1]
Output: 1
```

```
Example 2: 

Input: [4,1,2,1,2]
Output: 4

```

### How to solve 

**Approach 1:** 

Use math, 2 * (a + b + c) - 2 * (a + b) = c

**Approach 2:** 

Use hashmap, collections.Counter()

**Approach 3:** 

Use hashmap, collections.defaultdict(int)

**Approach 4:** 

Bit Manipulation

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number1.py)

```python
return sum(set(nums)) * 2 - sum(nums)
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number2.py)

```python
hashmap = collections.Counter(nums)

for n in nums:
    if hashmap[n] == 1:
        return n
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number3.py)

```python
hash_table = collections.defaultdict(int)
for i in nums:
    hash_table[i] += 1

for i in hash_table:
    if hash_table[i] == 1:
        return i
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number4.py)

```python
a = 0
for n in nums:
    a ^= n
    
return a
```
