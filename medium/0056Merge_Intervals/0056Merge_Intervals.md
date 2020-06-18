## Merge Intervals

### Problem Link

https://leetcode.com/problems/merge-intervals/

### Problem Description 

Given a collection of intervals, merge all overlapping intervals.

```
Example 1:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

```
Example 2:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

```

**Note:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

### How to solve 

**Approach 1:**

先排序, 再消边


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0056Merge_Intervals/0056Merge_Intervals1.py)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return intervals
        
        intervals = sorted(intervals, key = lambda x : x[0])
        output = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if right >= intervals[i][1]:
                continue
            if right >= intervals[i][0]:
                right = intervals[i][1]
            else:
                output.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        output.append([left, right])
            
        return output
```
