"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        int_a = 0
        int_b = 0
        
        digit = 0
        for bit in a[::-1]:
            int_a += 2 ** digit * int(bit)
            digit += 1
        digit = 0
        for bit in b[::-1]:
            int_b += 2 ** digit * int(bit)
            digit += 1
        
        return str(bin(int_a + int_b))[2:]


if __name__ == '__main__':
    s = Solution()

    a = "1010"
    b = "1011"

    print(s.addBinary(a, b))