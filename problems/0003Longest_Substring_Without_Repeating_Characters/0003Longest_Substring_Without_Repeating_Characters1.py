"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	return collections.Counter(s) == collections.Counter(t)


if __name__ == '__main__':
    a = Solution()

    s = "anagram"
    t = "nagaram"

    print(s)
    print(t)
    print(a.isAnagram(s, t))


    
