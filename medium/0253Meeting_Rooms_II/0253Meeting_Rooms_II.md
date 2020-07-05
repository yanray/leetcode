## Coin Change

### Problem Link

https://leetcode.com/problems/coin-change/

### Problem Description 

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

```
Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

```

```
Example 2:

Input: coins = [2], amount = 3
Output: -1

```

**Note:**
You may assume that you have an infinite number of each kind of coin.

### Code (python)

[Approach 1: DP] (85%)

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
```

https://leetcode.com/problems/coin-change/discuss/481775/RZ-Summary-of-different-solutions-in-Python

[Approach 2: BFS] (85%)

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount <= 0:
            return 0
        
        coins = set(coins)
        level = [amount]
        visited = set([amount])
        count = 0
        while level:
            count += 1
            temp = []
            for a in level:
                if a in coins:
                    return count
                for c in coins:
                    if a - c > 0 and (a - c) not in visited:
                        temp.append(a - c)
                        visited.add(a - c)
            level = temp
        return -1
```