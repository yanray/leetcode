"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        see_once = {}
        for i, ch in enumerate(s):
            if ch in see_once:
                see_once[ch] = -1
            else:
                see_once[ch] = i

        for v in see_once.values():
            if v != -1:
                return v
                
        return -1


if __name__ == '__main__':
    a = Solution()

    s = "leetcode"

    print(a.firstUniqChar(s))


    
