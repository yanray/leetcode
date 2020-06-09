"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        new_s = ""
        
        length_s = len(s)
        index = 0
        curr_row = 1
        compare_row = 1
        for i in range(length_s):
            new_s += s[index]
            if curr_row == 1 or curr_row == numRows:
                index += 2 * (numRows - curr_row) + 2 * (curr_row - 1)
            # elif curr_row == numRows:
                # index += 2 * (curr_row - 1)
            else:
                index += 2 * abs(compare_row - curr_row)
                if compare_row == numRows:
                    compare_row = 1
                else:
                    compare_row = numRows
            if index >= length_s:
                curr_row += 1
                compare_row = numRows
                index = curr_row - 1
                
        return new_s


if __name__ == '__main__':
    a = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    print("old string", s)
    print("new string", a.convert(s, numRows))
    
