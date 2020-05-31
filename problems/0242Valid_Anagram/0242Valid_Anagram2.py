"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	return sorted(s) == sorted(t)


if __name__ == '__main__':
    a = Solution()

    s = "anagram"
    t = "nagaram"

    print(s)
    print(t)
    print(a.isAnagram(s, t))


    
