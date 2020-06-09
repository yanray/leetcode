"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

import re 

class Solution:
    def myAtoi(self, str: str):
        
        match = re.match('[ ]*([+-]?\d+)', str)
        if match:
            i = int(match.group(1))            
            return min(i, 2**31-1) if i >=0 else max(i, -2**31) 
        else:
            return 0



if __name__ == '__main__':

    a = Solution()

    s = "   -42"
    print("input:", s)
    print("output:", a.myAtoi(s))







