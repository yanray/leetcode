"""

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1


if __name__ == '__main__':
    a = Solution()

    s = "leetcode"

    print(a.firstUniqChar(s))


    
