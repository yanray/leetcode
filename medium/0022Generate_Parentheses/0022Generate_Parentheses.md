## Generate Parentheses

### Problem Link

https://leetcode.com/problems/next-permutation/

### Problem Description 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

```
Example 1:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

```

### Code (python)

[Approach 1] (95% - 98)

```python
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            print(S)
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
```