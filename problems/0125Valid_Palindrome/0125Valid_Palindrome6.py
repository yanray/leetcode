"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]


if __name__ == '__main__':
    a = Solution()

    s = "A man, a plan, a canal: Panama"

    print(a.isPalindrome(s))

