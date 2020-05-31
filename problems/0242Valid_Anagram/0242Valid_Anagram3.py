"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char in s: 
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
        return False not in [char_count[char] == 0 for char in char_count]


if __name__ == '__main__':
    a = Solution()

    s = "anagram"
    t = "nagaram"

    print(s)
    print(t)
    print(a.isAnagram(s, t))


    
