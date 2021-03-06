## Spiral Matrix

### Problem Link

https://leetcode.com/problems/spiral-matrix/

### Problem Description 

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

```
Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

```

```
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```

### Code (python)

[Approach 1] (90%)

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return matrix
        
        spiral = []
        spiral = spiral + matrix[0]
        row = 1
        row_limit, col_limit = [1, len(matrix) - 1], [0, len(matrix[0]) - 1]
        direct = "Down"
        count = 1
        while len(spiral) < len(matrix) * len(matrix[0]):
            if direct == "Down":
                while row < row_limit[1]:
                    spiral.append(matrix[row][col_limit[1]])
                    row += 1
                row -= 1
                spiral = spiral + matrix[row_limit[1]][col_limit[0] : col_limit[1] + 1][::-1]
                row_limit[1] -= 1
                col_limit[1] -= 1

                direct = "Up"
                
            elif direct == "Up":
                while row > row_limit[0]:
                    spiral.append(matrix[row][col_limit[0]])
                    row -= 1
                row += 1
                spiral = spiral + matrix[row_limit[0]][col_limit[0] : col_limit[1] + 1]
                row_limit[0] += 1
                col_limit[0] += 1
                
                direct = "Down"
        
        return spiral
```

[Approach 2] (80%)

```python
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
```

[Approach 3: Layer-by-Layer]

```python
class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans
```

https://leetcode.com/problems/spiral-matrix/discuss/720401/Python3-straightforward-solution-Spiral-Matrix

https://leetcode.com/problems/spiral-matrix/discuss/685000/Python-Simple-solution-peeling-off-layers

https://leetcode.com/problems/spiral-matrix/discuss/629683/Very-Simple-Solution-Beats-99.83

https://leetcode.com/problems/spiral-matrix/discuss/496148/Python3-easy-to-understand-solution-with-comments

https://leetcode.com/problems/spiral-matrix/discuss/440442/Easy-to-remember-Python3

https://leetcode.com/problems/spiral-matrix/discuss/435612/Python3-Try-Except