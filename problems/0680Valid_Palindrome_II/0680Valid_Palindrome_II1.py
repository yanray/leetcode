"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            return s == s[::-1]
        
        if s == s[::-1]:
            return True
        
        first, last = 0, len(s) - 1
        
        while first < last:
            if s[first] != s[last]:
                return isPalindrome(s[first + 1 : last + 1]) or isPalindrome(s[first : last])
            first += 1
            last -= 1
            
        return True

if __name__ == '__main__':
    a = Solution()

    s = "eedede"
    print(a.validPalindrome(s))

