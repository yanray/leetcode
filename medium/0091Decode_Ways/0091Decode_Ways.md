## Decode Ways

### Problem Link

https://leetcode.com/problems/decode-ways/

### Problem Description 

A message containing letters from A-Z is being encoded to numbers using the following mapping:

```
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
```

Given a non-empty string containing only digits, determine the total number of ways to decode it.

```
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

```

```
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

```

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