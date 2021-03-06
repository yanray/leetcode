## Remove All Adjacent Duplicates In String

### Problem Link

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

### Problem Description 

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

```
Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

**Note:**

1. 1 <= S.length <= 20000
2. S consists only of English lowercase letters.

### Code (python)

[Approach 1] (24%) 

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        if len(S) <= 1:
            return S
        
        ss = list(map(str, S))
        
        i = 0
        j = 1
        
        while j < len(ss):
            
            if ss[i] == ss[j]:
                ss.pop(j)
                ss.pop(i)
                i -= 1
                j -= 1
                if i < 0:
                    i = 0
                    j = 1
            else:
                i += 1
                j += 1
            
        return "".join(ss)
```

(41%)

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i=0
        while i+1<len(s):
            if s[i+1]==s[i]:
                s=s[:i]+s[i+2:]
                if i>=1:
                    i-=1
            else:
                i+=1
        return s
```

[Approach 2: Regular Expression] (81%)

```python
import re

class Solution:
    def removeDuplicates(self, S: str) -> str:
        regex = re.compile(r'([a-z])\1')
        
        while regex.search(S):
            S = regex.sub('', S)
        return S
```

[Approach 3: Stack] (72%) (fast)

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if not stack or stack[-1] != ch: 
                stack.append(ch)  
            else: 
                stack.pop()
        return "".join(stack)
```

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return S
        res = [S[0]]
        for curr in S[1:]:            
            if res and curr == res[-1]:
                res.pop()
            else:
                res.append(curr)
        res = ''.join(res)                
        return res
```