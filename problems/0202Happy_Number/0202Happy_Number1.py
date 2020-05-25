"""

Version: 1.1 
Author:  Yanrui 
date:    5/23/2020
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        before_nums = []
        n_sum = n
        
        while n_sum != 1: 
            n = n_sum
            n_sum = 0

            if n in before_nums:
                return False

            before_nums.append(n)
            while n >= 1:
                n_sum = n_sum + pow(n % 10, 2)
                n = int(n / 10)
            
        return True



if __name__ == '__main__':
    a = Solution()

    n = 19
    print(a.isHappy(n))





