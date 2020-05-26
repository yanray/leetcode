"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
      return x >= 0 and x == int(str(x)[::-1])
      # return x >= 0 and x == int(f"{x}"[::-1])


if __name__ == '__main__':
    a = Solution()

    print(a.isPalindrome(121))