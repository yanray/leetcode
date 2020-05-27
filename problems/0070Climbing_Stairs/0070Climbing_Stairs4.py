"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import math

class Solution:
    def climbStairs(self, n: int) -> int:

    	def dfs(n):
    		if n not in memo: memo[n] = dfs(n-1)+dfs(n-2)
    		return memo[n]   

    	memo = {1:1, 2:2}
    	return dfs(n)


if __name__ == '__main__':
    a = Solution()

    n = 10
    print(a.climbStairs(n))

