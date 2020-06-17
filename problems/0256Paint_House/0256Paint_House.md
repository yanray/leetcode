## Paint House

### Problem Link

https://leetcode.com/problems/two-sum/

### Problem Description 

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

**Note:**
All costs are positive integers.

```
Example 1:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.

```

### How to solve 

**Approach 1:**

Dynamic Programming

**Approach 2:**

Brute force with a Recursive Tree

**Approach 3:**

Memoization


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0256Paint_House/0256Paint_House1.py)

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        if not costs:
            return 0
        
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        
        return min(costs[-1])
```

```python
def minCost(self, costs: List[List[int]]) -> int:
	if not costs: return 0
	dp = costs[0]
	for i in range(1, len(costs)):
		a = costs[i][0]+min(dp[1], dp[2])
		b = costs[i][1]+min(dp[0], dp[2])
		c = costs[i][2]+min(dp[0], dp[1])
		dp = [a, b, c]
	return min(dp)
```

```python
import copy

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        if len(costs) == 0: return 0

        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):

            current_row = copy.deepcopy(costs[n])
            # Total cost of painting nth house red?
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green?
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue?
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)

```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0256Paint_House/0256Paint_House2.py)

```python
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0: # Red
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1: # Green
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else: # Blue
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0256Paint_House/0256Paint_House3.py)

```python
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        def paint_cost(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost

        if costs == []:
            return 0

        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
```


```python
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        @lru_cache(maxsize=None)
        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
```

[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0256Paint_House/0256Paint_House4.py)

```python
class Solution:
    # O(1) space, shorter version, can be applied 
    # for more than 3 colors
    def minCost(self, costs):
        if not costs:
            return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            pre = dp[:] # here should take care
            for j in range(len(costs[0])):
                dp[j] = costs[i][j] + min(pre[:j]+pre[j+1:])
        return min(dp)
```