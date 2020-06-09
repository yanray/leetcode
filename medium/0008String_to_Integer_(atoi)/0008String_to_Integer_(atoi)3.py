"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

import re 

class Solution:
    def myAtoi(self, str: str):
        
        s = str.lstrip()        
        potential_nums = re.findall("[\+\-]{0,1}[0-9]+", s)
        
        if len(potential_nums) == 0:
            return 0
        if not s[0].isnumeric():
            if s[0] not in ['+', '-'] or not s[1].isnumeric():
                return 0
        
        return min(max(int(potential_nums[0]), -(2 ** 31)), 2 ** 31 - 1)



if __name__ == '__main__':

    a = Solution()

    s = "   -42"
    print("input:", s)
    print("output:", a.myAtoi(s))







