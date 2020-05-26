## Palindrome Number

### Problem Link
https://leetcode.com/problems/palindrome-number/

### Problem Description 

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


```
Example 1:

Input: 121
Output: true

```

```
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```


```
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

**Follow up:**

Coud you solve it without converting the integer to a string?


### How to solve 

**Approach 1:** 

to string 

**Approach 2:** 



### Code (python)

[Approach 1]()

```python
return x >= 0 and x == int(str(x)[::-1])
# return x >= 0 and x == int(f"{x}"[::-1])
```

[Approach 2]

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
