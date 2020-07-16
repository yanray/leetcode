## Maximal Square

### Problem Link

https://leetcode.com/problems/maximal-square/

### Problem Description 

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

```
Example 1:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


```


### Code (python)

[Approach 1] (%) 

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        nr = len(matrix)
        nc = len(matrix[0])
        
        if nr < 2:
            for i in range(nc):
                if matrix[0][i] == "1":
                    return 1
            return 0
        elif nc < 2:
            for i in range(nr):
                if matrix[i][0] == "1":
                    return 1
            return 0
        
        max_area = max(int(matrix[0][0]), int(matrix[0][1]), int(matrix[1][0]))
        for i in range(1, nr):
            for j in range(1, nc):
                if matrix[i][j] == "1":
                    val = min(int(matrix[i - 1][j - 1]), int(matrix[i - 1][j]), int(matrix[i][j - 1])) + 1
                    max_area = max(max_area, val)
                    matrix[i][j] = str(val)
        
        return max_area ** 2
```

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
    
        n, m = len(matrix), len(matrix[0])
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        max_square = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                print(dp)
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_square = max(max_square, dp[i][j])    
                    
        return max_square ** 2
```