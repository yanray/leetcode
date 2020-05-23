"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def reverse(self, x):
        
        upper_limit = 2 ** 31 - 1
        lower_limit = -2 ** 31
        
        str_x = str(x)
        if x >= 0:
            rev_x = int(str_x[::-1])
        else:
            rev_x = int("-" + str_x[1:][::-1])
            
        return rev_x if rev_x < upper_limit and rev_x > lower_limit else 0 


if __name__ == '__main__':
    a = Solution()

    num = 123
    print('Input: ', num)
    print('Output:', a.reverse(num))


