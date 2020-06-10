"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ''
        for i in range(len(s)):
            maxPal = max(maxPal, self.largestPalindrome(s, i-1, i), self.largestPalindrome(s,i-1,i+1), key=len)
        return maxPal
        
    def largestPalindrome(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return s[i+1:j]


if __name__ == '__main__':
    a = Solution()

    s = "babad"

    print("string: ", s)
    print("output: ", a.longestPalindrome(s))
    
