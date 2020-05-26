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

to string 

**Approach 2:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0009Palindrome_Number/0009Palindrome_Number1.py)

```python
return x >= 0 and x == int(str(x)[::-1])
# return x >= 0 and x == int(f"{x}"[::-1])
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0009Palindrome_Number/0009Palindrome_Number2.py)

```python
def reverse_num(x):
    rev_x = 0
    while x > 0:
        rev_x, x = rev_x * 10 + x % 10, x // 10
        
    return rev_x

if x < 0:
    return False

return x == reverse_num(x)
```
