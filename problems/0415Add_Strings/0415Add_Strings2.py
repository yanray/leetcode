"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def addStrings(self, num1, num2):
        int_num1 = 0
        for i in range(len(num1)):
            int_num1 = int_num1 * 10 + ord(num1[i]) - ord('0')
            
        int_num2 = 0
        for i in range(len(num2)):
            int_num2 = int_num2 * 10 + ord(num2[i]) - ord('0')
            
        return str(int_num1 + int_num2)


if __name__ == '__main__':
    a = Solution()

    num1 = '1325'
    num2 = '25219'

    print('num1: ', num1)
    print('num2: ', num2)
    print('num1 + num2:', a.addStrings(num1, num2))


