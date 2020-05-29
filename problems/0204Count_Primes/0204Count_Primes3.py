"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution:
    def countPrimes(self, n):
        if n < 3: return 0
        dp = [0, 0] + [1] * (n - 2)
        for i in range(2, int(n ** 0.5) + 1):
            if dp[i]: dp[i ** 2:n:i] = [0] * len(dp[i ** 2:n:i])
        return sum(dp)
            

if __name__ == '__main__':
    a = Solution()


    n = 10
    print(a.countPrimes(n))

