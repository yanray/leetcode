"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


if __name__ == '__main__':
    a = Solution()

    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = []
    print(a.longestCommonPrefix(strs))

