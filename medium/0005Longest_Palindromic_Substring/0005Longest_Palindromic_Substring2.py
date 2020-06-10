"""

Version: 1.1 
Author:  Yanrui 
date:    06/08/2020
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, max_len, n= '', 0, len(s)
        dp = [[0]*n for _ in range(n)]

        print(dp)
        for i in range(n):
            dp[i][i] = 1
            res = s[i]
            max_len = 1

        print(dp)
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res = s[i:i+2]
                max_len = 2

        print(dp)
        for i in range(n):
            for j in range(i-1):
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = 1
                    if i-j+1>max_len:
                        max_len = i-j+1
                        res = s[j:i+1]
        return res


if __name__ == '__main__':
    a = Solution()

    s = "babad"

    print("string: ", s)
    print("output: ", a.longestPalindrome(s))
    
