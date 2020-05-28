"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(r'[^a-zA-Z0-9]')
        return s2 == s2[::-1]


if __name__ == '__main__':
    a = Solution()

    s = "A man, a plan, a canal: Panama"

    print(a.isPalindrome(s))

