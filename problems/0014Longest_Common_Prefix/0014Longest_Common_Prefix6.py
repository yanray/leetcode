"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import os
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res, i, j = '', 0, 0
        try:
            while True:
                if i == len(strs) - 1:
                    res += strs[0][j]
                    i = 0
                    j += 1
                if strs[i][j] == strs[i+1][j]:
                    i += 1
                else:
                    return res
        except:
            return res


if __name__ == '__main__':
    a = Solution()

    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = []
    print(a.longestCommonPrefix(strs))

