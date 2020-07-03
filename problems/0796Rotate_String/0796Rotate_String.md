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

[Approach 2: KMP (Knuth-Morris-Pratt)] (%)

```python
class Solution:
    def rotateString(self, A, B):
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        #Compute shift table
        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        #Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False
```

```python
def lps(pat):
    lps = [0]*len(pat)
    j = 0
    i=1
    while i<len(pat):
        if pat[j]==pat[i]:
            j+=1
            lps[i]=j
        elif j>0:
            j = lps[j-1]
            i-=1
        else:
            lps[i]=0
        i+=1
    return lps

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)!=len(B): return False
        if len(A)==0: return True
        shift = lps(B)
        A = A+A
        i=j=0
        while i<len(A) and j<len(B):
            if A[i]!=B[j] and j>0:
                j=shift[j-1]
                i-=1
            else:
                j+=1
            i+=1
            if j==len(B): return True
        return False
```