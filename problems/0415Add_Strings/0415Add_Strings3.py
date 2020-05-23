"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def addStrings(self, num1, num2):
        str_to_int_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    
        int_num1 = 0
        len_num1 = len(num1)
        for i in range(len_num1):
            int_num1 += 10 ** (len_num1 -1 - i) * str_to_int_dict[num1[i]]
            
        int_num2 = 0
        len_num2 = len(num2)
        for i in range(len_num2):
            int_num2 += 10 ** (len_num2 -1 - i) * str_to_int_dict[num2[i]]
            
        return str(int_num1 + int_num2)


if __name__ == '__main__':
    a = Solution()

    num1 = '123'
    num2 = '222'


    print('num1: ', num1)
    print('num2: ', num2)
    print('num1 + num2:', a.addStrings(num1, num2))


