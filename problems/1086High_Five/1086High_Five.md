## High Five

### Problem Link

https://leetcode.com/problems/high-five/

### Problem Description 

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.


```
Example 1: 

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

```

**Note:**

1. 1 <= items.length <= 1000
2. items[i].length == 2
3. The IDs of the students is between 1 to 1000
4. The score of the students is between 1 to 100
5. For each student, there are at least 5 scores


### How to solve 

**Approach 1:** 

Use hashmap

**Approach 2:** 

Use heap

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/1086High_Five/1086High_Five1.py)

```python
import numpy as np

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        high_five_dict = {}
        for i in range(len(items)):
            if items[i][0] in high_five_dict:
                if items[i][1] > high_five_dict[items[i][0]][0]:                    
                    bisect.insort(high_five_dict[items[i][0]], items[i][1])
                    high_five_dict[items[i][0]].pop(0)
            else:
                high_five_dict[items[i][0]] = [0, 0, 0, 0, items[i][1]]
            
        output = []
        for k, v in high_five_dict.items():
            output.append([k, int(np.mean(v))])
        
        return output
```

```python
import numpy as np

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        high_five_dict = {}
        for i in range(len(items)):
            if items[i][0] in high_five_dict:
                if items[i][1] > high_five_dict[items[i][0]][0]:
                    high_five_dict[items[i][0]][0] = items[i][1]
                    high_five_dict[items[i][0]].sort()
            else:
                high_five_dict[items[i][0]] = [0, 0, 0, 0, items[i][1]]
            
        output = []
        for k, v in high_five_dict.items():
            output.append([k, int(np.mean(v))])
        
        return output
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/1086High_Five/1086High_Five2.py)

```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # use collectioni for hashmap
        import collections
        # use heapq to get only top 5 values
        import heapq

        d = collections.defaultdict(list)
        # print(d)

        for idx, val in items:
            # adding values for each id in hashmap
            heapq.heappush(d[idx], val)
            # print(idx, val, d)

            if len(d[idx]) > 5:
                # print("if")
                # heappop pops the smallest value
                # so we alway has the length 5 for each id
                heapq.heappop(d[idx])
                # print(d)

        # print([[i, sum(d[i]) // 5] for i in sorted(d)])
        ans = [[i, sum(d[i]) // 5] for i in sorted(d)]
        return ans

```
