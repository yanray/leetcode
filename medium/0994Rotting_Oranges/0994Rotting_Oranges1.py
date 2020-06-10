"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ convert s to st in the following manner to eliminate even odd conditin palindrom 
        s = abc st = $#a#b#c#%"""
        st = ''
        for i in range(len(s)):
            st += '#'+ s[i]
        st = '$'+st+'#%'
        
        P = [0]*len(st)
        C,R = 0, 0
        for i in range(1, len(st)-1):
            mirr = 2*C-i
            
            # update already expanded palindrome
            if i < R:
                P[i] = min(R-i, P[mirr])
            
            while st[i+(1+P[i])] == st[i-(1+P[i])]:
                P[i] += 1
            
            if i+P[i] > R:
                C = i
                R = i + P[i]
        
        # extract the longest palindromic substring from P, st
        length = max(P)
        index = P.index(length)
        string = st[index-length:index+length]
        return string.replace('#','')


if __name__ == '__main__':
    a = Solution()

    s = "babad"

    print("string: ", s)
    print("output: ", a.longestPalindrome(s))
    
