"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x, y = int(a, 2), int(b, 2)

        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


if __name__ == '__main__':
    s = Solution()

    a = "1010"
    b = "1011"

    print(s.addBinary(a, b))