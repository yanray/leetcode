## Game of Life

### Problem Link

https://leetcode.com/problems/game-of-life/

### Problem Description 

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population..
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Given a non-empty string containing only digits, determine the total number of ways to decode it.

```
Example 1:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

```

**Follow up:**

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

### Code (python)

[Approach 1] (78%) 

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1


        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
```

```python
class Solution:
	def numDecodings(self, S: str) -> int:
		if not S or S[0] == "0":
			return 0
		dp = [S[0],1,0,1] #"[pre_str, single_end_nums, combine_end_nums, total_nums ]"
    
		for s in S[1:]:
			temp = [s,0,0,0]
			temp[1] = dp[3] if 1 <= int(s) <= 9 else 0
			temp[2] = dp[1] if 1 <= int(dp[0]+s) <= 26 else 0
			temp[3] = temp[1] + temp[2]
			if temp[3] == 0:
				return 0
			dp = temp[:]
		return dp[3]
```

https://leetcode.com/problems/decode-ways/discuss/441486/Simple-clear-Python-limit-space-DP-solution

[Approach 2: Recursive Approach with Memoization]   (O(N))

```python
class Solution:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s)-1:
            return 1

        # Memoization is needed since we might encounter the same sub-string.
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index+1, s) + (self.recursive_with_memo(index+2, s) if (int(s[index : index+2]) <= 26) else 0)

        # Save for memoization
        self.memo[index] = ans

        return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recursive_with_memo(0, s)
```


https://leetcode.com/problems/decode-ways/discuss/570071/Python3-easy-and-faster-than-57.84

https://leetcode.com/problems/decode-ways/discuss/375152/Python-with-fibonacci-function-O(1)-memory-fast