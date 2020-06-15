## Nested List Weight Sum

### Problem Link

https://leetcode.com/problems/nested-list-weight-sum/

### Problem Description 

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.


```
Example 1: 

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.

```

```
Example 2: 

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

```

### How to solve 

**Approach 1:** 

DFS


### Code (python)

[Approach 1]()

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def DFS(nestedList, layer) -> int:
            sum_val = 0
            for nest in nestedList:
                if nest.isInteger():
                    sum_val += layer * nest.getInteger()
                else:
                    sum_val += DFS(nest.getList(), layer + 1)
            return sum_val
        

        layer = 1
        return DFS(nestedList, layer)
```
