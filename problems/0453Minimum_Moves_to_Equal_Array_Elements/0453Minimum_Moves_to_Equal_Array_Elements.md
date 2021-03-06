## Minimum Moves to Equal Array Elements

### Problem Link

https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

### Problem Description 

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

```
Example 1:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

```

### Code (python)

[Approach 1] (34%) 

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0
        
        nums.sort()
        
        moves = 0
        count = 1
        for i in range(len(nums) - 1, 0, -1):
            moves += count * (nums[i] - nums[i - 1])
            count += 1
            
        return moves
```

[Approach 3: Using Sorting] (41%)  O(nlog(n))

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums.sort()
        
        moves = 0
        for i in range(len(nums) - 1, 0, -1):
            moves += nums[i] - nums[0]
            
        return moves
```

[Approach 4: Using DP] (25%)  O(nlog(n))

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums.sort()
        
        moves = 0
        for i in range(1, len(nums)):
            diff = moves + nums[i] - nums[i - 1]
            nums[i] += moves
            moves += diff
            
        return moves
```

[Approach 5: Using Math] (25%)  O(N)

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        min_val = min(nums)
        
        moves = 0
        for i in range(len(nums)):
            moves += nums[i] - min_val
            
        return moves
```

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)
```