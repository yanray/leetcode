"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

import re 

class Solution:
    def myAtoi(self, str: str):
        
        def helper(x):
            if not x: return 0
            ret = 0
            for i in x:
                if not i.isdigit(): return ret
                ret = ret *10 + int(i)
            return ret

        s = str.strip()
        if not s: return 0
        elif s[0] == '+': return min(2**31-1,helper(s[1:]))
        elif s[0] == '-': return max(-2**31,-helper(s[1:]))
        elif s[0].isdigit(): return min(2**31-1,helper(s))
        else: return 0



if __name__ == '__main__':

    a = Solution()

    s = "   -42"
    print("input:", s)
    print("output:", a.myAtoi(s))







