"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

import re 

class Solution:
    def myAtoi(self, str: str):
        
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)

if __name__ == '__main__':

    a = Solution()

    s = "   -42"
    print("input:", s)
    print("output:", a.myAtoi(s))







