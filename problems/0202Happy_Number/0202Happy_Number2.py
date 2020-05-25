"""

Version: 1.1 
Author:  Yanrui 
date:    5/23/2020
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_num(n):
            n_sum = 0
            while n != 0:
                n, mod = divmod(n, 10)
                n_sum += mod ** 2
            return n_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next_num(n)
            
        return n == 1


if __name__ == '__main__':
    a = Solution()

    n = 2
    print(a.isHappy(n))





