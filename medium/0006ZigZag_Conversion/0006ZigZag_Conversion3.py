"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        curr_row = 0
        direction = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[curr_row] += s[i]
            if numRows > 1:
                curr_row += direction
                if curr_row == 0 or curr_row == numRows -1:
                    direction *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr


if __name__ == '__main__':
    a = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    print("old string", s)
    print("new string", a.convert(s, numRows))
    
