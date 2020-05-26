"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def reverse_num(x):
            rev_x = 0
            while x > 0:
                rev_x, x = rev_x * 10 + x % 10, x // 10
                
            return rev_x
        
        if x < 0:
            return False
        
        return x == reverse_num(x)


if __name__ == '__main__':
    a = Solution()

    print(a.isPalindrome(121))