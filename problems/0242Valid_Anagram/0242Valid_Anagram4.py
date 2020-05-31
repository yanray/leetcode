"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = {}
        
        for c in s:
            firstWord[c] = firstWord[c] + 1 if c in firstWord else 1
        
        for c in t:
            if c not in firstWord:
                return False
            
            firstWord[c] = firstWord[c] - 1
            
            if firstWord[c] <= 0:
                del firstWord[c]
            
        return len(firstWord) == 0


if __name__ == '__main__':
    a = Solution()

    s = "anagram"
    t = "nagaram"

    print(s)
    print(t)
    print(a.isAnagram(s, t))


    
