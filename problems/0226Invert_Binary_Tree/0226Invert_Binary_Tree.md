## Invert Binary Tree

### Problem Link

https://leetcode.com/problems/invert-binary-tree/

### Problem Description 

Invert a binary tree.

```
Example 1:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

```

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

[Approach 2] (%)

```python

```