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
        
        slow_runner = n
        fast_runner = get_next_num(n)
        while fast_runner != 1 and fast_runner != slow_runner:
            slow_runner = get_next_num(slow_runner)
            fast_runner = get_next_num(get_next_num(fast_runner))
            
        return fast_runner == 1


if __name__ == '__main__':
    a = Solution()

    n = 2
    print(a.isHappy(n))





