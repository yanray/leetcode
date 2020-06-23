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

[Approach 1] (95% - 98%)

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

(80-98%)

```python
class Solution(object):
    def generate(self, n, openParenthesis, closeParenthesis, result, s):
        if openParenthesis == n and closeParenthesis == n:
            result.append(s)
            return
        
        if openParenthesis >= closeParenthesis:
            if openParenthesis < n:
                temp = s + "("
                self.generate(n, openParenthesis+1, closeParenthesis, result, temp)
            if closeParenthesis < n:
                temp = s + ")"
                self.generate(n, openParenthesis, closeParenthesis+1, result, temp)
            
    def generateParenthesis(self, n):
        s = ""
        result = []
        self.generate(n, 0, 0, result, s)
        
        return result
        
        """
        :type n: int
        :rtype: List[str]
        """

```

(DFS)

[Approach 2] (92% - 98%)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.dfs('', n, n)
        return self.ans

    def dfs(self, pre, left, right):
        if right == 0:
            self.ans.append(pre)
        if left:
            self.dfs(pre + '(', left - 1, right)
        if right > left:
            self.dfs(pre + ')', left, right - 1)
```

(BFS)

[Approach 3] (92% - 98%)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # For element in queue, it means (pre-string, left, right)
        queue = collections.deque([('', n, n)])
        while queue:
            pre, left, right = queue.popleft()
            if right == 0:
                ans.append(pre)
            if left:
                queue.append((pre + '(', left - 1, right))
            if right > left:
                queue.append((pre + ')', left, right - 1))
        return ans
```

(Closure Number)

[Approach 3] (92% - 98%)

```python
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```