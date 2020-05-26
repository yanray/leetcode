## Add Binary

### Problem Link
https://leetcode.com/problems/add-binary/

### Problem Description 

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.


```
Example 1:

Input: a = "11", b = "1"
Output: "100"

```

```
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

```

**Constraints:**

* Each string consists only of '0' or '1' characters.
* 1 <= a.length, b.length <= 10^4
* Each string is either "0" or doesn't contain any leading zero.


**Follow up:**

Coud you solve it without converting the integer to a string?


### How to solve 

**Approach 1:** 

Change to int, add sum, change back binary

**Approach 2:** 

improved of Approach 2

**Approach 3:** 

Use Bit to compute directly

**Approach 4:** 

Bit Manipulation:

* Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.

* While carry is nonzero: y != 0:

    Current answer without carry is XOR of x and y: answer = x^y.

    Current carry is left-shifted AND of x and y: carry = (x & y) << 1.

    Job is done, prepare the next loop: x = answer, y = carry.

* Return x in the binary form.


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0067Add_Binary/0067Add_Binary1.py)

```python
int_a = 0
int_b = 0

digit = 0
for bit in a[::-1]:
    int_a += 2 ** digit * int(bit)
    digit += 1
digit = 0
for bit in b[::-1]:
    int_b += 2 ** digit * int(bit)
    digit += 1

return str(bin(int_a + int_b))[2:]
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0067Add_Binary/0067Add_Binary2.py)

```python
return "{0:b}".format(int(a, 2) + int(b, 2))
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0067Add_Binary/0067Add_Binary3.py)

```python
str_sum = ""
length = max(len(a), len(b))
a, b = a.zfill(length), b.zfill(length)

carry = 0
for i in range(length - 1, -1, -1):
    if a[i] == "1":
        carry += 1
    if b[i] == "1":
        carry += 1
        
    if carry % 2 == 0:
        str_sum += "0"
    else:
        str_sum += "1"
        
    carry //= 2
    
if carry == 1:
    str_sum += "1"
    
return str_sum[::-1]
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0067Add_Binary/0067Add_Binary3.py)

```python
str_sum = ""
length = max(len(a), len(b))
a, b = a.zfill(length), b.zfill(length)

carry = 0
for i in range(length - 1, -1, -1):
    if a[i] == "1":
        carry += 1
    if b[i] == "1":
        carry += 1
        
    if carry % 2 == 0:
        str_sum += "0"
    else:
        str_sum += "1"
        
    carry //= 2
    
if carry == 1:
    str_sum += "1"
    
return str_sum[::-1]
```

