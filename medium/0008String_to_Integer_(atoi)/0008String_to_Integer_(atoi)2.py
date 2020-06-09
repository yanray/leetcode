"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

import re 

class Solution:
    def myAtoi(self, str: str):
        
        str = str.lstrip()

        if not str:
            return 0

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if str[0] == "+" or str[0] == "-":
            new_str = re.match("^\d+", str[1:])
            if new_str == None:
                return 0
            else:
                num = int(str[0] + new_str.group())
                if num >= 0:
                    return num if num <= INT_MAX else INT_MAX
                else:
                    return num if num >= INT_MIN else INT_MIN

        if str[0].isdigit():
            new_str = re.match("^\d+", str)
            return int(new_str.group()) if int(new_str.group()) <= INT_MAX else INT_MAX

        else:
            return 0



if __name__ == '__main__':

    a = Solution()

    s = "   -42"
    print("input:", s)
    print("output:", a.myAtoi(s))







