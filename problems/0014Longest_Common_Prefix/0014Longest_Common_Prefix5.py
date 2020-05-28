"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import os
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        return os.path.commonprefix(strs)


if __name__ == '__main__':
    a = Solution()

    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = []
    print(a.longestCommonPrefix(strs))

