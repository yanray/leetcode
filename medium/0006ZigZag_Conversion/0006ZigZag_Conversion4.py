"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows > len(s):  # corner case
            return s
        res, i, step = ['' for r in range(numRows)], 0, 0  # a string for each line
        for ch in s:
            res[i] += ch
            if i == 0:  # first row
                step = 1  # down
            if i == numRows - 1:  # last row
                step = -1  # up
            i += step
        return "".join(res)


if __name__ == '__main__':
    a = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    print("old string", s)
    print("new string", a.convert(s, numRows))
    
