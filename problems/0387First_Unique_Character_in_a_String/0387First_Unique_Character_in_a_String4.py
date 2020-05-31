"""

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
      counts = dict()
      
      for char in s:
        counts[char] = counts.get(char, 0) + 1
      
      for i in range(0, len(s)):        
        if counts[s[i]] == 1:
          return i
      
      return -1

if __name__ == '__main__':
    a = Solution()

    s = "leetcode"

    print(a.firstUniqChar(s))


    
