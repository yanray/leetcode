"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

class Solution:
    def climbStairs(self, n: int) -> int:

        ways = 0
        first = 1
        second = 2
        
        if n == 1:
            return first
        elif n == 2:
            return second
        else:
            for i in range(2, n):
                ways = first + second
                first = second
                second = ways

        return ways

if __name__ == '__main__':
    a = Solution()

    n = 5
    print(a.climbStairs(n))

