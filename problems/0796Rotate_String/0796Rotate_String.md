## Rotate String

### Problem Link

https://leetcode.com/problems/rotate-string/

### Problem Description 

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

```
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

```

**Note:**

* A and B will have length at most 100.

### Code (python)

[Approach 1] (73%)

```python
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        if not A and not B:
            return True
        elif not A or not B:
            return False
        
        def check_str_equal(s1, s2):
            return s1 == s2
        
        for i in range(len(B)):
            if B[i] == A[0]:
                if check_str_equal(B[i : ] + B[: i], A):
                    return True
                
        return False
```

https://www.cnblogs.com/wade-luffy/p/7716358.html

[Approach 2] (%)

```python

```