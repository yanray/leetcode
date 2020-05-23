"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def reverse(self, x):
        
        lower_limit = -pow(2, 31)
        upper_limit = pow(2, 31) - 1
        
        rev_x = 0
        if x < 0:
            sign = -1
            x = -x
        else: 
            sign = 1

        while x != 0:
            x, temp = divmod(x, 10)
            rev_x = rev_x * 10 + temp
        rev_x = rev_x * sign
            
        return rev_x if rev_x < upper_limit and rev_x > lower_limit else 0 


if __name__ == '__main__':
    a = Solution()

    num = 123
    print('Input: ', num)
    print('Output:', a.reverse(num))


