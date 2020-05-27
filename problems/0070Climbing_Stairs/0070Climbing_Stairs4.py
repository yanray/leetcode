"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

class Solution:
    def climbStairs(self, n: int) -> int:

    	def helper(n: int) -> int:
    		if n < 3:
    			return n
    		elif n not in memo:
    			memo[n] = helper(n-1) + helper(n-2)
    		return memo[n]

    	memo = {}
    	return helper(n)


if __name__ == '__main__':
    a = Solution()

    n = 10
    print(a.climbStairs(n))

