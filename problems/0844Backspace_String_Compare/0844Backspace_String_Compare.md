## Pascal's Triangle

### Problem Link

https://leetcode.com/problems/pascals-triangle/

### Problem Description 

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

```
Example 1:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

```


### Code (python)

[Approach 1] (98%)

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle_list = []
        for i in range(1, numRows + 1):
            row_list = [1] * i
            for j in range(1, i - 1):
                row_list[j] = triangle_list[i - 2][j - 1] + triangle_list[i - 2][j]
            triangle_list.append(row_list)

        return triangle_list
```

Solution

https://leetcode.com/problems/pascals-triangle/discuss/?currentPage=1&orderBy=hot&query=&tag=python3