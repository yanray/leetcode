## Implement strStr()

### Problem Link

https://leetcode.com/problems/implement-strstr/

### Problem Description 

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

```
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

```

```
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

```

**Clarification:**

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


### Code (python)

[Approach 1] (20%)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        def check_equal(s1, s2):
            return s1 == s2
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if check_equal(haystack[i : i + len(needle)], needle):
                    return i
                
        return -1
```

```python
class Solution:
    def strStr(self, haystack, needle):
        n, h = len(needle), len(haystack)
        hash_n = hash(needle)
        for i in range(h-n+1):
            if hash(haystack[i:i+n]) == hash_n:
                return i
        return -1
```

https://leetcode.com/problems/implement-strstr/discuss/665448/AC-simply-readable-Python-KMP-Rabin-Karp

[Approach 2: KMP] (21%)

```python
class Solution:
    def strStr(self, haystack, needle):
        n, h = len(needle), len(haystack)
        i, j, nxt = 1, 0, [-1]+[0]*n
        while i < n:                                # calculate next array
            if j == -1 or needle[i] == needle[j]:   
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]

        print(nxt)
        i = j = 0
        while i < h and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]
        return i-j if j == n else -1
```