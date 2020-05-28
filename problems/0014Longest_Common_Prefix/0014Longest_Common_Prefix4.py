"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

if __name__ == '__main__':
    a = Solution()

    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = []
    print(a.longestCommonPrefix(strs))

