"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import math

class Solution:
    def climbStairs(self, n: int) -> int:

        def fib(n):
            sqrt5 = math.sqrt(5)
            Fn = (1 / sqrt5) * (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n)

            return int(Fn)
        return fib(n + 1)


if __name__ == '__main__':
    a = Solution()

    n = 10
    print(a.climbStairs(n))

