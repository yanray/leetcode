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
        
        index = 0
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        if str[index] == "-" and (index + 1) < len(str) and str[index + 1].isdigit():
            new_str = str[index] + str[index + 1]
            index += 2
            while index < len(str) and str[index].isdigit():
                new_str += str[index]
                index += 1

            return int(new_str) if int(new_str) >= INT_MIN else INT_MIN 
        
        elif str[index] == "+" and (index + 1) < len(str) and str[index + 1].isdigit():
            new_str = str[index] + str[index + 1]
            index += 2
            while index < len(str) and str[index].isdigit():
                new_str += str[index]
                index += 1

            return int(new_str) if int(new_str) <= INT_MAX else INT_MAX

        elif str[index].isdigit():
            new_str = str[index]
            index += 1
            while index < len(str) and str[index].isdigit():
                new_str += str[index]   
                index += 1
            return int(new_str) if int(new_str) <= INT_MAX else INT_MAX
        
        else:
            return 0



if __name__ == '__main__':

    a = Solution()

    s = "   -42"
    print("input:", s)
    print("output:", a.myAtoi(s))







