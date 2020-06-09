"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s 
        n = len(s)
        cycle = 2*numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                strlist.append(s[j])
                if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                    strlist.append(s[j+cycle-2*i])             
        newstr = ''.join(strlist)
        return newstr


if __name__ == '__main__':
    a = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    print("old string", s)
    print("new string", a.convert(s, numRows))
    
