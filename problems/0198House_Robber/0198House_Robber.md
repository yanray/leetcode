## House Robber

### Problem Link

https://leetcode.com/problems/house-robber/

### Problem Description 

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


```
Example 1: 

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

```

```
Example 2: 

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

```

### How to solve 

**Approach 1:** 

if len(nums) > 4, dp[i] += max(dp[i - 2], dp[i - 3])
给nums前边补4个0即可满足all conditions

**Approach 2:** 

dp[k] = max{ dp[k-1], dp[k-2] + i }

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0198House_Robber/0198House_Robber1.py)

```python
nums = [0, 0, 0, 0] + nums
    
for i in range(3, len(nums)):
    nums[i] += max(nums[i - 2], nums[i - 3])
    
return max(nums)
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0198House_Robber/0198House_Robber2.py)

```python
prev = 0
curr = 0
# every loop, calculate the maximum cumulative amount of money until current house
for i in nums:
    # as the loop begins，curr represents dp[k-1]，prev represents dp[k-2]
    # dp[k] = max{ dp[k-1], dp[k-2] + i }
    prev, curr = curr, max(curr, prev + i)
    # as the loop ends，curr represents dp[k]，prev represents dp[k-1]

return curr
```


