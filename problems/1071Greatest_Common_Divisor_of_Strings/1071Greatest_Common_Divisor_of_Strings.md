## Greatest Common Divisor of Strings

### Problem Link

https://leetcode.com/problems/greatest-common-divisor-of-strings/

### Problem Description 

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

```
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

```

```
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

```

```
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

```
 
**Note:**

1. 1 <= str1.length <= 1000
2. 1 <= str2.length <= 1000
3. str1[i] and str2[i] are English uppercase letters.


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