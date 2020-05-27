"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        sum_int = 0
        i = 0
        while i < (len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                sum_int += roman_dict[s[i + 1]] - roman_dict[s[i]]
                i += 2
            else:
                sum_int += roman_dict[s[i]]
                i += 1
        if i != len(s):
            sum_int += roman_dict[s[-1]]
        
        return sum_int

if __name__ == '__main__':
    a = Solution()

    s = "MCMXCIV"
    print(a.romanToInt(s))

