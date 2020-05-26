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




### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0009Palindrome_Number/0009Palindrome_Number1.py)

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

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0009Palindrome_Number/0009Palindrome_Number2.py)

```python
return "{0:b}".format(int(a, 2) + int(b, 2))
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0009Palindrome_Number/0009Palindrome_Number2.py)

```python
return "{0:b}".format(int(a, 2) + int(b, 2))
```
